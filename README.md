# DIP_programming

# Command:
Create a virtual environment in the terminal
```
py -m venv .venv
```

Upgrade pip:
```
py -m pip install --upgrade pip
```

Set-Execution Policy to allow the current user to execute scripts as follows
```
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

```
pip install pyautogui
```

Install packages
```
pip install -r .\requirements.txt
```

Freeze packages
``
python -m pip freeze > requirements.txt
```

# Some problems:
Transfer variable from a frame to another frame. 
Solution: init them with updated grandparent before deploying.

Problem 2: labelimg -> Re-Opening the app resets classes.txt 
Solution: https://github.com/heartexlabs/labelImg/issues/482
```
def change_save_dir_dialog(self, _value=False):

    if self.default_save_dir is not None:
        path = ustr(self.default_save_dir)
    else:
        path = '.'

    dir_path = ustr(QFileDialog.getExistingDirectory(self,
                                                     '%s - Save annotations to the directory' % __appname__, path,  QFileDialog.ShowDirsOnly
                                                     | QFileDialog.DontResolveSymlinks))
    
    ```ruby
    if os.path.exists(dir_path + "/classes.txt"):
        self.label_hist = None
        self.load_predefined_classes(dir_path + "/classes.txt")
    ```
    
    if dir_path is not None and len(dir_path) > 1:
        self.default_save_dir = dir_path

    self.statusBar().showMessage('%s . Annotation will be saved to %s' %
                                 ('Change saved folder', self.default_save_dir))
    self.statusBar().show()
```
Notice: Open dir and Change Save dir whenever re-opening