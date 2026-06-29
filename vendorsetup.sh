# ROM source patches

color="\033[0;32m"
end="\033[0m"

echo -e "${color}Applying patches${end}"
sleep 1

# HALS
echo -e "${color}cloning audio HAL ${end}"
rm -rf hardware/qcom-caf/sm8250/audio
git clone https://github.com/muralivijay/android_hardware_qcom_audio.git -b lineage-23.2-caf-sm8250 hardware/qcom-caf/sm8250/audio

echo -e "${color}cloning display HAL ${end}"
rm -rf hardware/qcom-caf/sm8250/display
git clone https://github.com/muralivijay/android_hardware_qcom_display.git -b lineage-23.2-caf-sm8250 hardware/qcom-caf/sm8250/display

# Sepolicy fix for imsrcsd
echo -e "${color}Switch back to legacy imsrcsd sepolicy${end}"
rm -rf device/qcom/sepolicy_vndr/legacy-um/qva/vendor/bengal/ims/imsservice.te
cp device/qcom/sepolicy_vndr/legacy-um/qva/vendor/bengal/legacy-ims/hal_rcsservice.te device/qcom/sepolicy_vndr/legacy-um/qva/vendor/bengal/ims/hal_rcsservice.te
