#!/usr/bin/env sh
# warning: script should be used after installing package control
# (otherwise it will not install other packages defined in "Package Control.sublime-settings")


dir_src="https://raw.githubusercontent.com/smirnovkirilll/lookmomimadataengineer/main/sublime_settings/"
dir_tgt_osx="${HOME}/Library/Application\ Support/Sublime\ Text/Packages/User/"
dir_tgt_linux="${HOME}/.config/sublime-text/Packages/User/"
settings_to_copy=(
  "Anaconda.sublime-settings"
  "Default (Linux).sublime-mousemap"
  "Default (OSX).sublime-mousemap"
  "MarkdownPreview.sublime-settings"
  "Package Control.sublime-settings"
  "PlainTasks.sublime-settings"
  "Preferences.sublime-settings" )

# 1. choose target dir
if [[ ! -d $dir_tgt_osx ]]; then
  dir_tgt=$dir_tgt_linux
fi

# 2. download
for setting in "${settings_to_copy[@]}"; do
  # download (convert spaces to "%20" in urls)
  curl "${dir_src}${setting// /%20}" -o "${dir_tgt}${setting}"
done

echo "sublime settings downloaded to system specific config directory"
