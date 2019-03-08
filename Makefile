all:
	dmd -release computeAllD.d
	nim c -d:release computeAllNim.nim
	rustc -C opt-level=2 compute-all-rust.rs
	go build compute-all-go.go
