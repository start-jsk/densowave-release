Name:           ros-hydro-denso-launch
Version:        0.2.9
Release:        0%{?dist}
Summary:        ROS denso_launch package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/denso_launch
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-checkerboard-detector
Requires:       ros-hydro-control-msgs
Requires:       ros-hydro-denso-controller
Requires:       ros-hydro-vs060-moveit-config
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-control-msgs
BuildRequires:  ros-hydro-denso-controller
BuildRequires:  ros-hydro-rostest
BuildRequires:  ros-hydro-vs060-moveit-config

%description
Although the package name might indicate that it only could only contain generic
.launch files, this package functions as a center location for storing .launch
files for all DENSO robots (currently vs060).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sat Mar 07 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.9-0
- Autogenerated by Bloom

* Wed Jul 30 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.8-0
- Autogenerated by Bloom

