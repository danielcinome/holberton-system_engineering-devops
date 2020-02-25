#!/usr/bin/env ruby
a = ARGV[0].scan(/from:(\w+|.\d+)/).join
b = ARGV[0].scan(/to:(.\d+)/).join
c = ARGV[0].scan(/flags:(.\d+:(\d+|.\d+):.\d+:(\d+|.\d+):.\d+)/).join
puts("#{a},#{b},#{c}")
