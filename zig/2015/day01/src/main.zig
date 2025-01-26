const std = @import("std");

fn pt1(path: []const u8) !isize {
    var floor: isize = 0;

    const allocator = std.heap.page_allocator;

    // optimize n to the length of the file if known
    const memory = try allocator.alloc(u8, 8000);
    defer allocator.free(memory);

    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();

    const data = try file.readToEndAlloc(allocator, std.math.maxInt(usize));

    for (data) |c| {
        switch (c) {
            '(' => floor += 1,
            ')' => floor -= 1,
            else => unreachable,
        }
    }

    return floor;
}

fn pt2(path: []const u8) !usize {
    var floor: isize = 0;
    var pos: usize = 0;

    const allocator = std.heap.page_allocator;

    // optimize n to the length of the file if known
    const memory = try allocator.alloc(u8, 8000);
    defer allocator.free(memory);

    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();

    const data = try file.readToEndAlloc(allocator, std.math.maxInt(usize));

    for (data) |c| {
        pos += 1;
        switch (c) {
            '(' => floor += 1,
            ')' => floor -= 1,
            else => unreachable,
        }
        if (floor == -1) {
            return pos;
        }
    }
    return pos;
}

pub fn main() !void {
    // create stdout writer
    const stdout_file = std.io.getStdOut().writer();
    var bw = std.io.bufferedWriter(stdout_file);
    const stdout = bw.writer();

    // print part 1 result
    try stdout.print("Part 1: {}\n", .{try pt1("input.txt")});
    try bw.flush();

    // print part 2 result
    try stdout.print("Part 2: {}\n", .{try pt2("input.txt")});
    try bw.flush();
}

test "pt1 test " {
    const expected: comptime_int = 0;
    const actual = try pt1("test_input.txt");
    try std.testing.expectEqual(expected, actual);
}

test "pt2 test" {
    const expected: comptime_int = 5;
    const actual = try pt2("test_input2.txt");
    try std.testing.expectEqual(expected, actual);
}
