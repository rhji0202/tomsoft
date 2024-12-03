# -*- mode: python ; coding: utf-8 -*-

block_cipher = None  # 암호화가 필요한 경우 여기에 설정할 수 있음.

# 애플리케이션 분석
a = Analysis(
    ['main.py'],  # 메인 스크립트
    pathex=[],  # 프로젝트 경로 (필요시 수정)
    binaries=[],  # 추가적인 바이너리 파일이 있으면 여기에 추가
    datas=[],  # 템플릿을 datas에 포함시키지 않음
    hiddenimports=[],  # 자동으로 감지되지 않은 의존성 모듈이 있으면 추가
    hooksconfig={},  # 사용자 정의 hook이 있으면 여기에 설정
    runtime_hooks=[],  # 런타임 훅 설정
    excludes=[],  # 제외할 모듈들
    noarchive=False,  # 아카이브를 사용하지 않으려면 True로 설정
    optimize=0,  # 최적화 수준 (0-3, 기본은 0)
)

# 순수 Python 코드 압축
pyz = PYZ(a.pure, cipher=block_cipher)

# 실행 파일 설정
exe = EXE(
    pyz,  # 순수 Python 코드 압축 결과
    a.scripts,  # 스크립트 목록
    a.binaries,  # 포함할 바이너리 파일
    a.datas,  # 포함할 데이터 파일 (현재는 비워둠)
    [],
    name='WebViewer',  # 생성될 실행 파일 이름
    debug=True,  # 디버그 모드 활성화 (개발 시 유용)
    bootloader_ignore_signals=False,  # 신호 무시 여부 (디버그 시 False)
    strip=False,  # 불필요한 심볼 제거 여부 (False로 설정하면 디버깅 용이)
    upx=True,  # UPX 압축 사용 여부
    upx_exclude=[],  # 압축에서 제외할 파일들
    runtime_tmpdir=None,  # 임시 디렉토리 설정
    console=True,  # 콘솔 창을 띄울지 여부 (GUI 애플리케이션이라면 False)
    disable_windowed_traceback=False,  # GUI에서 발생한 에러 트레이스백 표시 여부
    argv_emulation=False,  # 명령행 인자 에뮬레이션 사용 여부
    target_arch=None,  # 타겟 아키텍처 설정 (특정 아키텍처에 맞추려면 설정)
    codesign_identity=None,  # 코드 서명 식별자 (macOS에서 사용)
    entitlements_file=None,  # 코드 서명 관련 권한 파일 (macOS에서 사용)
    distpath='./dist',  # 빌드된 실행 파일을 저장할 경로
    workpath='./build',  # 임시 빌드 파일이 저장될 경로
)

# templates 폴더를 dist 폴더에 복사하는 작업 추가
import shutil
shutil.copytree('output', './dist/output')

# 애플리케이션 번들 설정 (macOS에서 사용)
app = BUNDLE(
    exe,
    name='main.app',  # 최종 애플리케이션 번들의 이름
    icon=None,  # 애플리케이션 아이콘 (필요 시 설정)
    bundle_identifier=None,  # 번들 식별자 (필요 시 설정)
    distpath='./dist',  # 번들 파일이 저장될 디렉토리
    workpath='./build',  # 번들 빌드를 위한 임시 디렉토리
)
