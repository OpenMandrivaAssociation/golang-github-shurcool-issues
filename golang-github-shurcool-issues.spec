# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/issues
%global commit          c5ffda8383060586c180b557ba5de0274285853c

%global common_description %{expand:
Issues service definition for Go.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Issues service definition for Go.
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/google/go-github/github)
BuildRequires: golang(github.com/shurcooL/events)
BuildRequires: golang(github.com/shurcooL/events/event)
BuildRequires: golang(github.com/shurcooL/githubv4)
BuildRequires: golang(github.com/shurcooL/notifications)
BuildRequires: golang(github.com/shurcooL/reactions)
BuildRequires: golang(github.com/shurcooL/users)
BuildRequires: golang(github.com/shurcooL/users/asanaapi)
BuildRequires: golang(github.com/shurcooL/webdavfs/vfsutil)
BuildRequires: golang(github.com/tambet/go-asana/asana)
BuildRequires: golang(golang.org/x/build/maintner)
BuildRequires: golang(golang.org/x/net/webdav)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5-20181026gitc5ffda8
- Fix import

* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4-20181026gitc5ffda8
- Bump to commit c5ffda8383060586c180b557ba5de0274285853c

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitadf13e4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20180422gitadf13e4
- Upstream GIT adf13e46e3d966ef14ee08722b56b823cf5c3f3b

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180422git5076edd
- First package for Fedora

