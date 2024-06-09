# Create conda environment
echo "Creating new conda environment, yeah-trends, with Python 3.11..."
conda create --name yeah-trends python=3.11 -y

# Detect the shell and initialize conda accordingly
echo "Detecting shell and initializing conda..."
case "$SHELL" in
    */zsh)
        conda init zsh
        ;;
    */bash)
        conda init bash
        ;;
    */fish)
        conda init fish
        ;;
    */tcsh)
        conda init tcsh
        ;;
    *)
        echo "Unsupported shell. Please initialize conda manually."
        exit 1
        ;;
esac

# Activate the conda environment
# This requires sourcing the shell-specific initialization script
echo "Applying conda environment activation..."
echo "Current shell is $SHELL"
case "$SHELL" in
    */zsh)
        source ~/.zshrc
        ;;
    */bash)
        source ~/.bashrc
        ;;
    */fish)
        source ~/.config/fish/config.fish
        ;;
    */tcsh)
        source ~/.tcshrc
        ;;
esac

# Activate the conda environment
echo "Activating conda environment, yeah-trends..."
conda activate yeah-trends

# Install dependencies from requirements.txt
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt
