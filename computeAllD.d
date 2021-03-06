void main()
{
    import std.range, std.stdio;

    auto sum = 0.0;
    auto count = stdin.byLine
        .tee!(l => sum += l.length).walkLength;

    writeln("Average line length: ",
        count ? sum / count : 0);
}
