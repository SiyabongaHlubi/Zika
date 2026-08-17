import os

def generate_config_files():
    """Generate Zika_var6.xml through Zika_var100.xml based on Zika_var1.xml template"""
    
    # Read the template file
    with open('Zika_var1.xml', 'r') as f:
        template_content = f.read()
    
    # Generate config files 6-100
    for i in range(6, 101):
        # Replace the output file paths in the template
        new_content = template_content.replace('Zika_var1', f'Zika_var{i}')
        
        # Write the new config file
        filename = f'Zika_var{i}.xml'
        with open(filename, 'w') as f:
            f.write(new_content)
        
        print(f"Generated {filename}")
    
    print("All config files generated successfully!")

if __name__ == "__main__":
    generate_config_files()