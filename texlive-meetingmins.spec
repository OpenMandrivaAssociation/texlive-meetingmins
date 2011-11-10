# revision 24503
# category Package
# catalog-ctan /macros/latex/contrib/meetingmins
# catalog-date 2011-11-02 12:24:01 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-meetingmins
Version:	1.0
Release:	1
Summary:	Format written minutes of meetings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/meetingmins
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/meetingmins.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/meetingmins.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/meetingmins.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The class allows formatting of meeting minutes using \section
commands (which provide hierarchical structure). An agenda can
also be produced for distribution prior to the meeting, with
user-selected portions suppressed from printing.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/meetingmins/meetingmins.cls
%doc %{_texmfdistdir}/doc/latex/meetingmins/README
%doc %{_texmfdistdir}/doc/latex/meetingmins/meetingmins.pdf
%doc %{_texmfdistdir}/doc/latex/meetingmins/samples/agenda.pdf
%doc %{_texmfdistdir}/doc/latex/meetingmins/samples/agenda.tex
%doc %{_texmfdistdir}/doc/latex/meetingmins/samples/chair.pdf
%doc %{_texmfdistdir}/doc/latex/meetingmins/samples/chair.tex
%doc %{_texmfdistdir}/doc/latex/meetingmins/samples/department.min
%doc %{_texmfdistdir}/doc/latex/meetingmins/samples/minutes.pdf
%doc %{_texmfdistdir}/doc/latex/meetingmins/samples/minutes.tex
#- source
%doc %{_texmfdistdir}/source/latex/meetingmins/meetingmins.dtx
%doc %{_texmfdistdir}/source/latex/meetingmins/meetingmins.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
