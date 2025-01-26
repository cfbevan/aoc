const std = @import("std");
const input_reader = @import("input_reader.zig");

fn pt1(path: *const [0:0]u8) !usize {
    const allocator = std.heap.page_allocator;

    const memory = try allocator.alloc(u8, 1024);
    defer allocator.free(memory);

    const file = try std.fs.cwd().openFile(path, .{});
    defer file.close();

    const data = try file.readToEndAlloc(allocator, std.math.maxInt(usize));

    return data.len;
}

//fn pt2(path: *const [0:0]u8) !usize {
//    return 0;
//}

pub fn main() !void {
    // create stdout writer
    const stdout_file = std.io.getStdOut().writer();
    var bw = std.io.bufferedWriter(stdout_file);
    const stdout = bw.writer();

    // print part 1 result
    try stdout.print("Part 1: {}\n", .{pt1("input.txt")});
    try bw.flush();

    // print part 2 result
    //try stdout.print("Part 2: {}\n", .{pt2("input.txt")});
    //try bw.flush();
}

test "pt1 test" {
    const expected: comptime_int = 0;
    const actual = pt1("test_input.txt");
    try std.testing.expectEqual(expected, actual);
}

//test "pt2 test" {
//    const expected: comptime_int = 0;
//    const actual = pt2("test_input.txt");
//    try std.testing.expectEqual(expected, actual);
//}
