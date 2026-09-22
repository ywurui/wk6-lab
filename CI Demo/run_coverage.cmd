@echo off
pushd "%~dp0"
py -m coverage run -m unittest test_duckfine.py
popd
