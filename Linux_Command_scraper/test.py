import re

def clean_command_line(line):
    """
    Cleans a single line: removes prompts ($ or #), strips whitespace, 
    and removes trailing comments.
    """
    # Remove leading shell prompts (e.g., "$ ", "# ", "% ")
    line = re.sub(r"^\s*[\$#%]\s+", "", line)
    
    # Remove trailing comments (e.g., "sudo update # run this first")
    # We carefully look for ' #' to avoid breaking commands containing #
    if " #" in line:
        line = line.split(" #")[0]
        
    return line.strip()

def is_likely_command(cmd):
    """
    Heuristics to determine if a string is a command or just a variable/text.
    """
    if not cmd:
        return False
        
    parts = cmd.split()
    
    # If it's a multi-word string, it's likely a command (e.g., "git commit")
    if len(parts) > 1:
        return True
        
    # If it's a single word, it must be a common binary or contain a path slashe
    # This list can be expanded. It prevents capturing `wlan0` or `mywifi`.
    common_bins = {
        "ls", "cd", "pwd", "cp", "mv", "rm", "mkdir", "chmod", "chown", 
        "sudo", "su", "apt", "pacman", "yum", "dnf", "systemctl", 
        "service", "ip", "iw", "nmcli", "netctl", "git", "docker", 
        "kubectl", "grep", "cat", "nano", "vim", "vi", "top", "htop", "bash", "zsh"
    }
    
    if parts[0] in common_bins:
        return True
        
    if "/" in parts[0] or "./" in parts[0]: # Likely a script path
        return True
        
    return False

def extract_commands(text):
    """
    Robustly extracts Linux commands from mixed-format text.
    """
    extracted_lines = []

    # --- STRATEGY 1: Extract from Code Blocks (```bash ... ```) ---
    # We accept bash, sh, zsh, or no language specified
    code_blocks = re.findall(r"```(?:bash|sh|zsh)?\n(.*?)```", text, re.DOTALL)
    
    for block in code_blocks:
        lines = block.split('\n')
        for line in lines:
            cleaned = clean_command_line(line)
            if cleaned:
                extracted_lines.append(cleaned)

    # --- STRATEGY 2: Extract Inline Backticks (`...`) ---
    inline_code = re.findall(r"`([^`\n]+)`", text)
    for item in inline_code:
        cleaned = clean_command_line(item)
        # Apply strict filtering to inline items to avoid variables like `wlan0`
        if is_likely_command(cleaned):
            extracted_lines.append(cleaned)

    # --- STRATEGY 3: Detect "Loose" Commands (incorrectly formatted) ---
    # Looks for lines following the word "bash" or specific indentations
    raw_lines = text.split("\n")
    is_capturing = False
    
    for i, line in enumerate(raw_lines):
        line = line.strip()
        
        # Trigger: If line is explicitly "bash" or looks like a prompt start
        if line.lower() == "bash":
            is_capturing = True
            continue
            
        # Stop capturing on empty lines or headers
        if line == "" or line.startswith("#"):
            is_capturing = False
            continue
            
        if is_capturing:
            cleaned = clean_command_line(line)
            if is_likely_command(cleaned):
                extracted_lines.append(cleaned)

    # --- FINAL CLEANUP: Deduplicate while preserving order ---
    seen = set()
    final_commands = []
    
    for cmd in extracted_lines:
        if cmd not in seen:
            seen.add(cmd)
            final_commands.append(cmd)

    return "\n".join(final_commands)

# --- TEST DATA ---
text = """How to clean this data :
### Step 1: Install
First, open your terminal:

bash
sudo pacman -S wireless_tools iw netctl

This installs `wireless-tools`.

### Step 2: Configure
List networks:
bash
   sudo iw dev wlan0 scan | grep SSID

Replace `wlan0` with your interface.

2. **Enable**:
   `sudo netctl start mywifi`

### Step 3: Verify
$ nmcli device status wlan0
"""

# Execution
cleaned_commands = extract_commands(text)
print("-" * 20)
print("EXTRACTED SCRIPT:")
print("-" * 20)
print(cleaned_commands)
