import bz2
import base64
from pathlib import Path

papi_versions = [path.stem.replace('template-', '').replace('.papi', '') for path in Path('.').glob('template-*.papi')]

with open('papi_template.py', 'wt') as output_file:
    output_file.write(
        f'############################################################################\n'
        f'# This file is generated by {Path(__file__).name}, DO NOT EDIT !!!\n'
        f'############################################################################\n'
        f'import bz2\n'
        f'import base64\n'
        f'from pathlib import Path\n'
        f'\n'
        f'\n'
        f'PAPI_VERSIONS: list[str] = [\n')
    for papi_version in papi_versions:
        output_file.write(
            f'\t\'{papi_version}\',\n')
    output_file.write(
        f']\n'
        f'\n'
        f'\n'
        f'def create_empty_papi_database(file: Path, papi_version: str):\n'
        f'\tmatch papi_version:\n')
    for papi_version in papi_versions:
        with open(f'template-{papi_version}.papi', 'rb') as input_file:
            b64 = base64.b64encode(bz2.compress(input_file.read()))
            output_file.write(
                f'\t\tcase \'{papi_version}\':\n'
                f'\t\t\tb64 = (\n')
            part_len: int = 80
            for b64_part in [b64[i:i + part_len] for i in range(0, len(b64), part_len)]:
                output_file.write(
                    f'\t\t\t\t{b64_part}\n')
        output_file.write(
            f'\t\t\t)\n')
    output_file.write(
        f'\t\tcase _:\n'
        f'\t\t\traise ValueError()\n')
    output_file.write(
        f'\twith open(file, \'wb\') as f:\n'
        f'\t\tf.write(\n'
        f'\t\t\tbz2.decompress(\n'
        f'\t\t\t\tbase64.decodebytes(\n'
        f'\t\t\t\t\tb64\n'
        f'\t\t\t\t)\n'
        f'\t\t\t)\n'
        f'\t\t)\n')
