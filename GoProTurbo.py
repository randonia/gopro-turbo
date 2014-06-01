# Run through the given directories and rename each GoPro picture from 00001-99999.JPG

import os
import os.path
import signal
import shutil
import sys

def signal_handler(signal, frame):
    print 'Aborting process with CTRL-C'
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def validate_args():
    # TODO: Do better validation. Probably not manual
    if len(sys.argv) < 2:
        print "Not enough arguments"
        print_help()
        return False
    if not sys.argv[1]:
        # Verify it's a path?
        return False
    return True

def print_help():
    #TODO: Write a nicely formatted usage page
    print "======\nHere is where the help will be printed\n++++++"

def create_output_dir(directory):
    print "Creating ",directory
    os.system('mkdir -p "{0}"'.format(directory))

def move_file(in_dir, in_name, out_name, out_ext, out_dir):
    #tmp_file = "{0}{1}".format(str(out_name).zfill(6),out_ext)
    #os.system('touch {0}/{1}'.format(out_dir, tmp_file))
    #os.system('cp "{0}/{1}" "{2}/{3}.{4}"'.format(in_dir, in_name, out_dir, out_name, out_ext))
    src_file = '{0}/{1}'.format(in_dir, in_name)
    dest_file =  '{0}/{1}.{2}'.format(out_dir, str(out_name).zfill(8), out_ext)
    shutil.copy(src_file, dest_file)

# How many columns to print '.' 
STDOUT_COLS = 72

# TODO: Use some sort of detection for GoPro naming conventions
# http://gopro.com/support/articles/hero3-and-hero3-file-naming-convention
if validate_args():
    os_walk = os.walk(sys.argv[1])
    output_dir = "output_images"
    create_output_dir(output_dir)
    file_counter = 0
    file_extension = "JPG"
    
    for dirpath, dirnames, filenames in os_walk:
        if "GOPRO" in dirpath:
            print "Operating in folder: ", dirpath
            num_files = len(filenames)
            col_width = max(1,min(STDOUT_COLS,num_files))
            print "Found {0} images".format(num_files)
            for num, image_name in  enumerate(sorted(filenames)):
                if num % (num_files / col_width) == 0:
                    sys.stdout.write('.')
                    sys.stdout.flush()
                    
                full_file = "{0}/{1}".format(dirpath, image_name)
                move_file(dirpath, image_name, file_counter, file_extension, output_dir)
                file_counter += 1
            
            print ""

print "Done"
