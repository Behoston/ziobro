import re


def ziobro(major=0, minor=0, patch=0):
    return '0' * (major + 1) + '.' + '0' * (minor + 1) + '.' + '0' * (patch + 1)


def to_ziobro(semver):
    v = re.match(r'(?P<major>\d+)\.?(?P<minor>\d*)\.?(?P<patch>\d*)', semver)
    major = int(v.group('major'))
    minor = int(v.group('minor')) if v.group('minor') else 0
    patch = int(v.group('patch')) if v.group('patch') else 0
    return ziobro(major, minor, patch)
