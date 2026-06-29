#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/google/interfaces',
    'hardware/google/pixel',
    'hardware/lineage/interfaces/power-libperfmgr',
    'hardware/qcom-caf/bootctrl',
    'hardware/qcom-caf/common/libqti-perfd-client',
    'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys/display',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qualcomm.qti.dpm.api@1.0',
        'libmmosal',
        'vendor.qti.hardware.fm@1.0',
        'vendor.qti.hardware.wifidisplaysession@1.0',
        'vendor.qti.imsrtpservice@3.0',
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/lib64/vendor.qti.hardware.camera.postproc@1.0-service-impl.so': blob_fixup()
        .sig_replace('13 0A 00 94', '1F 20 03 D5'),
    'vendor/lib64/camera/components/com.qti.node.mialgocontrol.so': blob_fixup()
        .add_needed('libpiex_shim.so')
        .strip_debug_sections(),
    'vendor/lib64/libwvhidl.so': blob_fixup()
        .replace_needed('libcrypto.so', 'libcrypto-v34.so'),
    'vendor/lib64/libdpps.so': blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'spes',
    'xiaomi',
    blob_fixups=blob_fixups,
    check_elf=False,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
