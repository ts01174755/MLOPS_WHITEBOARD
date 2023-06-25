# Initialize LAST_PYTHONPATH
export LAST_PYTHONPATH="$(pwd):"

# Add this function to your .zshrc file
function chpwd() {
    local current_pyenv=$(pyenv version-name)
    if [[ ! -z "$LAST_PYTHONPATH" ]]; then
        # Remove the previous directory from PYTHONPATH if not in u'r setting environment
        export PYTHONPATH=$(echo $PYTHONPATH | sed -e "s|$LAST_PYTHONPATH||")
        # Update LAST_PYTHONPATH
        export LAST_PYTHONPATH=""
    fi
    if [[ "$(pyenv version-name)" != "system" ]]; then
        # Add the current directory to PYTHONPATH
        export PYTHONPATH="$(pwd):${PYTHONPATH}"
        # Update LAST_PYTHONPATH
        export LAST_PYTHONPATH="$(pwd):"
    fi
}


# Check if current environment what u want
if [[ "$(pyenv version-name)" != "system" ]]; then
    # Set initial PYTHONPATH
    export PYTHONPATH="$(pwd):"
fi
