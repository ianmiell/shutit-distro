# Begin Java addition
if ! [ -n "$MANPATH" ]; then
  export MANPATH=:/opt/jdk/man
else
  pathappend /opt/jdk/man       MANPATH
fi
# End Java addition
