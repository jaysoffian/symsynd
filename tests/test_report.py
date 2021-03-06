import os
import json
import pytest
from symsynd.report import ReportSymbolizer


def test_basic_report(res_path, driver):
    with open(os.path.join(res_path, 'crash-report.json')) as f:
        report = json.load(f)

    bt = None
    dsym_path = os.path.join(res_path, 'Crash-Tester.app.dSYM')
    rep = ReportSymbolizer(driver, dsym_path, report['binary_images'])
    for thread in report['crash']['threads']:
        if thread['crashed']:
            assert bt is None
            bt = rep.symbolize_backtrace(thread['backtrace']['contents'])

    assert bt is not None
    import pprint
    pprint.pprint(bt)
    assert bt == [
        {u'instruction_addr': 653426999,
         u'object_addr': 652337152,
         u'object_name': u'CoreFoundation',
         u'symbol_addr': 653426872,
         u'symbol_name': u'<redacted>'},
        {u'instruction_addr': 887639159,
         u'object_addr': 887611392,
         u'object_name': u'libobjc.A.dylib',
         u'symbol_addr': 887639120,
         u'symbol_name': u'objc_exception_throw'},
        {u'instruction_addr': 653448701,
         u'object_addr': 652337152,
         u'object_name': u'CoreFoundation',
         u'symbol_addr': 653448512,
         u'symbol_name': u'<redacted>'},
        {u'instruction_addr': 653440217,
         u'object_addr': 652337152,
         u'object_name': u'CoreFoundation',
         u'symbol_addr': 653439504,
         u'symbol_name': u'<redacted>'},
        {u'instruction_addr': 652585432,
         u'object_addr': 652337152,
         u'object_name': u'CoreFoundation',
         u'symbol_addr': 652585408,
         u'symbol_name': u'_CF_forwarding_prep_0'},
        {'column': 5,
         'filename': u'/Users/karl/Projects/KSCrash/Source/Common-Examples/Crasher.mm',
         u'instruction_addr': 782745,
         'line': 96,
         u'object_addr': 749568,
         u'object_name': u'Crash-Tester',
         u'symbol_addr': 749568,
         u'symbol_name': u'-[Crasher throwUncaughtNSException]',
         'uuid': u'8094558b-3641-36f7-ba80-a1aaabcf72da'},
        {'column': 11,
         'filename': u'/Users/karl/Projects/KSCrash/iOS/Crash-Tester/AppDelegate+UI.m',
         u'instruction_addr': 794881,
         'line': 358,
         u'object_addr': 749568,
         u'object_name': u'Crash-Tester',
         u'symbol_addr': 749568,
         u'symbol_name': u'__32-[AppDelegate(UI) crashCommands]_block_invoke',
         'uuid': u'8094558b-3641-36f7-ba80-a1aaabcf72da'},
        {'column': 5,
         'filename': u'/Users/karl/Projects/KSCrash/iOS/Crash-Tester/CommandTVC.m',
         u'instruction_addr': 802133,
         'line': 48,
         u'object_addr': 749568,
         u'object_name': u'Crash-Tester',
         u'symbol_addr': 749568,
         u'symbol_name': u'-[CommandEntry executeWithViewController:]',
         'uuid': u'8094558b-3641-36f7-ba80-a1aaabcf72da'},
        {'column': 5,
         'filename': u'/Users/karl/Projects/KSCrash/iOS/Crash-Tester/CommandTVC.m',
         u'instruction_addr': 803225,
         'line': 128,
         u'object_addr': 749568,
         u'object_name': u'Crash-Tester',
         u'symbol_addr': 749568,
         u'symbol_name': u'-[CommandTVC tableView:didSelectRowAtIndexPath:]',
         'uuid': u'8094558b-3641-36f7-ba80-a1aaabcf72da'},
        {u'instruction_addr': 711430419,
         u'object_addr': 710225920,
         u'object_name': u'UIKit',
         u'symbol_addr': 711429500,
         u'symbol_name': u'<redacted>'},
        {u'instruction_addr': 712146443,
         u'object_addr': 710225920,
         u'object_name': u'UIKit',
         u'symbol_addr': 712146248,
         u'symbol_name': u'<redacted>'},
        {u'instruction_addr': 710792953,
         u'object_addr': 710225920,
         u'object_name': u'UIKit',
         u'symbol_addr': 710792644,
         u'symbol_name': u'<redacted>'},
        {u'instruction_addr': 710246199,
         u'object_addr': 710225920,
         u'object_name': u'UIKit',
         u'symbol_addr': 710245732,
         u'symbol_name': u'<redacted>'},
        {u'instruction_addr': 653189741,
         u'object_addr': 652337152,
         u'object_name': u'CoreFoundation',
         u'symbol_addr': 653189720,
         u'symbol_name': u'<redacted>'},
        {u'instruction_addr': 653179217,
         u'object_addr': 652337152,
         u'object_name': u'CoreFoundation',
         u'symbol_addr': 653178940,
         u'symbol_name': u'<redacted>'},
        {u'instruction_addr': 653180243,
         u'object_addr': 652337152,
         u'object_name': u'CoreFoundation',
         u'symbol_addr': 653179328,
         u'symbol_name': u'<redacted>'},
        {u'instruction_addr': 652442017,
         u'object_addr': 652337152,
         u'object_name': u'CoreFoundation',
         u'symbol_addr': 652441540,
         u'symbol_name': u'CFRunLoopRunSpecific'},
        {u'instruction_addr': 652441523,
         u'object_addr': 652337152,
         u'object_name': u'CoreFoundation',
         u'symbol_addr': 652441416,
         u'symbol_name': u'CFRunLoopRunInMode'},
        {u'instruction_addr': 777949609,
         u'object_addr': 777912320,
         u'object_name': u'GraphicsServices',
         u'symbol_addr': 777949472,
         u'symbol_name': u'GSEventRunModal'},
        {u'instruction_addr': 710682261,
         u'object_addr': 710225920,
         u'object_name': u'UIKit',
         u'symbol_addr': 710680820,
         u'symbol_name': u'UIApplicationMain'},
        {'column': 12,
         'filename': u'/Users/karl/Projects/KSCrash/iOS/Crash-Tester/main.m',
         u'instruction_addr': 801763,
         'line': 17,
         u'object_addr': 749568,
         u'object_name': u'Crash-Tester',
         u'symbol_addr': 749568,
         u'symbol_name': u'main',
         'uuid': u'8094558b-3641-36f7-ba80-a1aaabcf72da'},
        {u'instruction_addr': 893569711,
         u'object_addr': 893562880,
         u'object_name': u'libdyld.dylib',
         u'symbol_addr': 893569708,
         u'symbol_name': u'<redacted>'}
    ]


@pytest.mark.xfail
def test_swift_report(res_path, driver):
    with open(os.path.join(res_path, 'swift-crash-report.json')) as f:
        report = json.load(f)

    bt = None
    dsym_path = os.path.join(res_path, 'Swift-Tester.app.dSYM')
    rep = ReportSymbolizer(driver, dsym_path, report['binary_images'])
    for thread in report['crash']['threads']:
        if thread['crashed']:
            assert bt is None
            bt = rep.symbolize_backtrace(thread['backtrace']['contents'])

    assert bt is not None
    assert bt == [
    ]
