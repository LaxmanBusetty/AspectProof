import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="93cf2a80-0a44-44f8-b934-94d5b6df092f",
    name="Subscribe to Trail Notes Newsletter",
    tc_id="TC-19",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"subscribed_message_visible": "true", "aspectproof_issues_seen_session": "0", "layout_report": "AspectProof layout\nPhone 390\u00d7844 (iPhone 14) \u00b7 portrait\nProbe: active (56 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=phone-390&run=r3-phone-390__signup&start=%2F', instruction_id='22a2ce5c-c565-4e1d-9edb-60bdfa2382ca'):
        await page.goto("http://localhost:4400/__ap/frame?profile=phone-390&run=r3-phone-390__signup&start=%2F")
    
    async with testmu.step('Waiting for the subscription form to be processed', instruction_id='89df7024-5a5d-4f43-bd6b-8464b8764338'):
        await page.wait_for_timeout(1000)
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "Test User" into "Name"', instruction_id='334d545a-f446-4e76-8b85-7b26c349a120'):
        element_0 = frame_0.locator("internal:role=textbox[name=\"Name\"i]")
        
        await testmu.fill(element_0, "Test User")
        # Reset to main page context
        frame_1 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "test@example.com" into "Email"', instruction_id='591d90c2-af7a-4c62-b2f5-97484d19a96b'):
        element_1 = frame_1.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_1, "test@example.com")
        # Reset to main page context
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Subscribe in the trail notes form', instruction_id='a7e38102-1dc1-476e-97bc-2e19367bc1af'):
        _loc_4 = frame_2.locator("internal:role=button[name=\"Subscribe\"i]")
        
        await _loc_4.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the subscription confirmation message is present'):
        set_var('subscribed_message_visible', await testmu.textual_analyzer(page, wrapped_js='(els) => {\n  const __m = {20: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(20).innerText.includes("You\'re subscribed"));\n  return (typeof __v === \'boolean\' ? String(__v) : __v);\n}', locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Thanks, Test User! You\'re"i'], query="whether a 'You're subscribed' message is present in the subscription form status message", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="a 'You're subscribed' message appears"))
    
    async with testmu.step('Reading the session issue count from the AspectProof layout panel'):
        set_var('aspectproof_issues_seen_session', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {28: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(28).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['#ap-seen'], query='the Issues seen this session count in the AspectProof layout panel', expected_value='0', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the "AspectProof layout" panel shows "Issues seen this session: 0"'))
    
    async with testmu.step('Extracting the full AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {24: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(24).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full panel text is stored as {{layout_report}}'))
    
    async with testmu.step('Assertion check', instruction_id='c58adff4-7cbb-4c74-9695-e1d748262fd0'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "a 'You're subscribed' message appears", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{subscribed_message_visible}}', 'store_key': 'subscribed_message_visible', 'variable_refs': {'{{subscribed_message_visible}}': 'true'}}], 'sub_checks': [{'description': "a 'You're subscribed' message appears", 'store_key': 'subscribed_message_visible', 'expected_value': 'true', 'extracted_value': '{{subscribed_message_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "a 'You're subscribed' message appears"})
    
    async with testmu.step('Assertion check', instruction_id='a2b368a4-bce5-4def-ad43-164b41b6c141'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'passed': True, 'operator': 'equals', 'transforms': ['strip'], 'json_path': None, 'expected': '0', 'extracted_value': '{{aspectproof_issues_seen_session}}', 'store_key': 'aspectproof_issues_seen_session', 'variable_refs': {'{{aspectproof_issues_seen_session}}': '0'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'store_key': 'aspectproof_issues_seen_session', 'expected_value': '0', 'extracted_value': '{{aspectproof_issues_seen_session}}', 'operator': 'equals', 'transforms': ['strip']}], 'composite_operator': 'and', 'claim': 'the "AspectProof layout" panel shows "Issues seen this session: 0"'})


if __name__ == "__main__":
    testmu.run(test)