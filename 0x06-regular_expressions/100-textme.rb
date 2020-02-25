#!/usr/bin/env ruby
a = ARGV[0].scan(/from:(\w+|.\d+)/).join
b = ARGV[0].scan(/to:(\w+|.\d+)/).join
c = ARGV[0].scan(/flags:([0-9.+-:]+)/).join
puts("#{a},#{b},#{c}")
