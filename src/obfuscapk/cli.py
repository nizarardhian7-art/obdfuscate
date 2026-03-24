#!/usr/bin/env python3

import argparse
import sys
import os
import logging

# Mapping display name ke module name
NAME_MAPPING = {
    'AdvancedReflection': 'advanced_reflection',
    'ArithmeticBranch': 'arithmetic_branch',
    'AssetEncryption': 'asset_encryption',
    'CallIndirection': 'call_indirection',
    'ClassRename': 'class_rename',
    'ConstStringEncryption': 'const_string_encryption',
    'DebugRemoval': 'debug_removal',
    'FieldRename': 'field_rename',
    'Goto': 'goto',
    'LibEncryption': 'lib_encryption',
    'MethodOverload': 'method_overload',
    'MethodRename': 'method_rename',
    'NewAlignment': 'new_alignment',
    'NewSignature': 'new_signature',
    'Nop': 'nop',
    'RandomManifest': 'random_manifest',
    'Rebuild': 'rebuild',
    'Reflection': 'reflection',
    'Reorder': 'reorder',
    'ResStringEncryption': 'res_string_encryption',
    'VirusTotal': 'virus_total',
}

def get_available_obfuscators():
    return sorted(NAME_MAPPING.keys())

def get_cmd_args():
    available_obfuscators = get_available_obfuscators()
    
    parser = argparse.ArgumentParser(description='Obfuscate an application (.apk/.aab) without needing its source code.')
    parser.add_argument('apk_or_bundle', help='The path to the application (.apk/.aab) to obfuscate')
    parser.add_argument('-o', '--obfuscator', action='append', required=True,
                        choices=available_obfuscators,
                        help='The name of the obfuscator to use.')
    parser.add_argument('-w', '--working-dir', help='The working directory')
    parser.add_argument('-d', '--destination', help='The path where to save the obfuscated file')
    parser.add_argument('-i', '--ignore-libs', action='store_true', help='Ignore known third party libraries')
    parser.add_argument('-p', '--show-progress', action='store_true', help='Show obfuscation progress')
    parser.add_argument('--use-aapt2', action='store_true', help='Use aapt2 for rebuild app')
    parser.add_argument('-k', '--virus-total-key', help='Virus Total API key')
    parser.add_argument('--keystore-file', help='Custom keystore file')
    parser.add_argument('--keystore-password', help='Keystore password')
    parser.add_argument('--key-alias', help='Key alias')
    parser.add_argument('--key-password', help='Key password')
    parser.add_argument('--ignore-packages-file', help='File with packages to ignore')
    return parser.parse_args()

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s> %(levelname)s][%(name)s][%(message)s')
    args = get_cmd_args()
    
    from obfuscapk.main import perform_obfuscation
    
    # Convert display name to module name
    obfuscator_list = [NAME_MAPPING[o] for o in args.obfuscator]
    print(f"Using obfuscators: {obfuscator_list}")
    
    # Call perform_obfuscation
    perform_obfuscation(
        args.apk_or_bundle,
        obfuscator_list,
        args.working_dir,
        args.destination,
        args.ignore_libs,
        args.show_progress,
        args.virus_total_key,
        args.keystore_file,
        args.keystore_password,
        args.key_alias,
        args.key_password,
        args.ignore_packages_file,
        args.use_aapt2
    )

if __name__ == '__main__':
    main()
