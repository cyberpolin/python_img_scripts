import os, shutil, subprocess, signal

for root, dirs, files in os.walk('.'):
  for dir in dirs:
    current_folder = './'+dir
    if dir != 'keeping':
      for root, dirs, files in os.walk(current_folder):
        for file in files:
          if ('1024' in file):
            print(file)
            img = subprocess.Popen(['open', current_folder+'/'+file])
            keep = raw_input('keep?')
            print(img.pid)
            os.kill(img.pid, signal.SIGKILL)
            if 'y' in keep:
              try:
                shutil.move(current_folder+'/'+file, './keeping')
                # shutil.rmtree(current_folder)
                print('keeping...')
              except Exception as e:
                raise e

            shutil.rmtree(current_folder)
