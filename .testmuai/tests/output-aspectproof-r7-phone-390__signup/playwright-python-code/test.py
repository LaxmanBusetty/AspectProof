import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="f3948df6-6f3d-4692-8452-a2e880300bd7",
    name="Subscribe to Trail Notes Newsletter",
    tc_id="TC-64",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"subscribed_message_visible": "true", "issues_seen_this_session": "Issues seen this session: 0", "layout_report": "AspectProof layout\nPhone 390\u00d7844 (iPhone 14) \u00b7 portrait\nProbe: active (62 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=phone-390&run=r7-phone-390__signup&start=%2F', instruction_id='bf648013-a213-47c3-acc5-97ea1b840ddb'):
        await page.goto("http://localhost:4400/__ap/frame?profile=phone-390&run=r7-phone-390__signup&start=%2F")
    
    async with testmu.step('Waiting for the queued subscription steps', instruction_id='35920739-685e-49a4-b46a-ca2275852136'):
        await page.wait_for_timeout(1000)
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "Test User" into "Name"', instruction_id='c42322c7-a933-4cde-bb0b-41c3f5dbab8e'):
        element_0 = frame_0.locator("internal:role=textbox[name=\"Name\"i]")
        
        await testmu.fill(element_0, "Test User")
        # Reset to main page context
        frame_1 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "test@example.com" into "Email"', instruction_id='4790b54e-cadc-484a-b880-e3867b46961b'):
        element_1 = frame_1.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_1, "test@example.com")
        # Reset to main page context
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Subscribe button in Get trail notes form', instruction_id='daaa29c3-907c-418b-95be-6d54323635b7'):
        _loc_4 = frame_2.locator("internal:role=button[name=\"Subscribe\"i]")
        
        await _loc_4.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the subscription confirmation message is present'):
        set_var('subscribed_message_visible', await testmu.textual_analyzer(page, wrapped_js='(els) => {\n  const __m = {20: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(20).innerText.includes("You\'re subscribed"));\n  return (typeof __v === \'boolean\' ? String(__v) : __v);\n}', locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Thanks, Test User! You\'re"i'], query="whether a 'You're subscribed' message is present in the subscription form status message", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="a 'You're subscribed' message appears."))
    
    async with testmu.step('Reading the session issue count from the layout panel'):
        set_var('issues_seen_this_session', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {27: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(27).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Issues seen this session:"i'], query='the Issues seen this session value in the AspectProof layout panel', expected_value='Issues seen this session: 0', needs_unit_conversion=False, operator='equals', transforms=[], condition='the "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Extracting the full AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {24: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(24).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full "AspectProof layout" panel text is stored as {{layout_report}}.'))
    
    async with testmu.step('Assertion check', instruction_id='4e706168-71b2-4dc0-8f76-fddf5e8c481f'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "a 'You're subscribed' message appears.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{subscribed_message_visible}}', 'store_key': 'subscribed_message_visible', 'variable_refs': {'{{subscribed_message_visible}}': 'true'}}], 'sub_checks': [{'description': "a 'You're subscribed' message appears.", 'store_key': 'subscribed_message_visible', 'expected_value': 'true', 'extracted_value': '{{subscribed_message_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "a 'You're subscribed' message appears."})
    
    async with testmu.step('Assertion check', instruction_id='88eb75bd-e953-4e7a-a498-c7221a885f8b'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'Issues seen this session: 0', 'extracted_value': '{{issues_seen_this_session}}', 'store_key': 'issues_seen_this_session', 'variable_refs': {'{{issues_seen_this_session}}': 'Issues seen this session: 0'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'issues_seen_this_session', 'expected_value': 'Issues seen this session: 0', 'extracted_value': '{{issues_seen_this_session}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'the "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)