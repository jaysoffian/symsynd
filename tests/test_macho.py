import os
from symsynd.macho import arch


def test_cpu_names():
    assert arch.get_cpu_name(12, 9) == 'armv7'


def test_uuid(res_path):
    ct_dsym_path = os.path.join(
        res_path, 'Crash-Tester.app.dSYM', 'Contents', 'Resources',
        'DWARF', 'Crash-Tester')
    uuids = arch.get_macho_uuids(ct_dsym_path)
    assert uuids == [
        ('armv7', '8094558b-3641-36f7-ba80-a1aaabcf72da'),
        ('arm64', 'f502dec3-e605-36fd-9b3d-7080a7c6f4fc'),
    ]
