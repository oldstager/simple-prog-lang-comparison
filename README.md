# Simple Programming Language and Compiler Comparison

This repo is used to showcase some programming languages (and compilers) source code and compilation results. Here's what I do to compile the source code:

```bash
D:
    dmd -release computeAllD.d
Nim:
    nim c -d:release computeAllNim.nim
Rust:
    rustc -C opt-level=3 compute-all-rust.rs
Go:
    go build compute-all-go.go
```

Source code for D and Nim was taken from their website. The result can be seen here (generated using [draw.py](draw.py)):

![Binary size result](compare-bin-size.png)

