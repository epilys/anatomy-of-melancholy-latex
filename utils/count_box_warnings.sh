#!/usr/bin/zsh

echo -n "Underfull vboxes: "
grep "Underfull .vbox" main.log | wc -l
echo -n "Underfull hboxes: "
grep "Underfull .hbox" main.log | wc -l
echo -n "Overfull vboxes: "
grep "Overfull .vbox" main.log | wc -l
echo -n "Overfull hboxes: "
grep "Overfull .hbox" main.log | wc -l
