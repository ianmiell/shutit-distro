# Begin /etc/profile.d/openjdk.sh

# Set JAVA_HOME directory
JAVA_HOME=/opt/jdk

# Set ANT_HOME directory
ANT_HOME=/opt/ant

# Adjust PATH
pathappend $JAVA_HOME/bin PATH
pathappend $ANT_HOME/bin PATH

# Auto Java CLASSPATH
# Copy jar files to, or create symlinks in this directory

AUTO_CLASSPATH_DIR=/usr/share/java

pathprepend . CLASSPATH

for dir in `find ${AUTO_CLASSPATH_DIR} -type d 2>/dev/null`; do
    pathappend $dir CLASSPATH
done

for jar in `find ${AUTO_CLASSPATH_DIR} -name "*.jar" 2>/dev/null`; do
    pathappend $jar CLASSPATH
done

export JAVA_HOME ANT_HOME CLASSPATH
unset AUTO_CLASSPATH_DIR dir jar

# End /etc/profile.d/openjdk.sh
