Name:           ros-hydro-denso-controller
Version:        0.2.8
Release:        0%{?dist}
Summary:        ROS denso_controller package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/denso_controller
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-open-controllers-interface
Requires:       ros-hydro-roscpp
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-open-controllers-interface
BuildRequires:  ros-hydro-roscpp

%description
This packages a common controller functionality for Denso's industrial
manipulators based on ORiN (Open Robot interface for the Network), a unified
network interface for industrial robot applications.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Jul 30 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.2.8-0
- Autogenerated by Bloom

