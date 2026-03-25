# OTP QR Decoder & Migration Parser
A Python-based utility designed to scan image files for QR codes, decode their contents, and specifically handle Google Authenticator migration strings. It provides a flexible interface that switches between a Command Line Interface (CLI) and a Graphical User Interface (GUI) based on how the script is launched.

# 🚀 Features
Dual-Mode Interface: Automatically detects if it is running in a terminal (stdin.isatty) or a GUI environment.

CLI Mode: Uses cooked_input for clean terminal prompts.

GUI Mode: Uses tkinter file and directory dialogs for a native OS feel.

QR Decoding: Utilizes pyzbar and Pillow to scan and extract data from various image formats.

OTP Migration Handling: Detects otpauth-migration:// URIs, unquotes the URL encoding, and decodes the underlying Base64 data.

Robust Logging: Uses logzero for formatted, timestamped debugging information.

## Requires the following packages:
* pybar
* PIL
* cooked_input
* logzerp
