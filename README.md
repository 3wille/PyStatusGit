# PyStatusGit

PyStatusGit is a module for i3pystatus displaying unstaged changes in a git respository.
The default displays changes in ``.dotfiles``

## Dependencies

* GitPython

## Install

``make`` will place a symlink to ``/usr/lib/python3.6/site-packages/i3pystatus/git_status.py``.
You need to take care of permissions yourself *cough*``sudo``*cough*.
If your python package path differs, just adapt the Makefile or place the file yourself.

## Usage

```python
status.register("git_status")
```

Optionally, pass a ``path``

```python
status.register("git_status", path="/home/foo/bar")
```
