"""Independent check of delivered PNG hashes, dimensions and every object's safe bounds."""
import copy
import hashlib
import json
import struct
from pathlib import Path

HERE = Path(__file__).resolve().parent


def inside(element, rect, padding=8):
    return (
        element['x'] - padding >= rect['x']
        and element['y'] - padding >= rect['y']
        and element['x'] + element['w'] + padding <= rect['x'] + rect['w']
        and element['y'] + element['h'] + padding <= rect['y'] + rect['h']
    )


def intersects(a, b, padding=8):
    return (
        a['x'] - padding < b['x'] + b['w']
        and a['x'] + a['w'] + padding > b['x']
        and a['y'] - padding < b['y'] + b['h']
        and a['y'] + a['h'] + padding > b['y']
    )


reports = sorted(HERE.glob('*_raport.json'))
assert len(reports) == 3
element_count = 0
for report_path in reports:
    report = json.loads(report_path.read_text())
    png_path = Path(str(report_path).replace('_raport.json', '.png'))
    png = png_path.read_bytes()
    assert png[:8] == b'\x89PNG\r\n\x1a\n'
    assert struct.unpack('>II', png[16:24]) == (report['width'], report['height'])
    assert hashlib.sha256(png).hexdigest() == report['sha256']
    assert report['geometryVerified'] is True
    assert report['officialMetaCurrentVerified'] is False  # Current source checks did not verify official data.
    assert not any(c['status'] == 'FAIL' for c in report['checks'])
    for element in report['objects']:
        if not element['important']:
            assert element['kind'] == 'logo'
            continue
        element_count += 1
        for profile in report['profileChecks']:
            assert inside(element, profile['safe']), (report_path.name, element['id'], profile['placement'])
            assert not any(intersects(element, block) for block in profile['blocked'])
    for check in report['checks']:
        if check['id'] == 'contrast-pixels':
            assert all(c['pass'] and c['pixels'] > 0 and c['ratio'] >= c['threshold'] for c in check['detail'])
    assert report['safeProfile']['kind'] == 'manual-screenshot-estimate'
    assert report['manualScreenshotCalibration']['officialVerification'] is False
    assert all(not o['intersections'] for o in report['manualScreenshotCalibration']['objects'])
    # Deliberately cross the boundary while keeping the element's center inside: it MUST fail.
    profile = report['profileChecks'][0]
    mutant = copy.deepcopy(next(e for e in report['objects'] if e['important']))
    mutant['x'] = profile['safe']['x'] - 1
    assert not inside(mutant, profile['safe'])
    print('PASS', png_path.name)
print(f'PASS: 3 PNG; {element_count} important text/icon objects, all selected placements; mutation detected.')
