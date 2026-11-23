import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="b192ea85-3f65-4ad8-8b48-fe1e45666bbf",
    name="Subscribe to Trail Notes and Verify Layout Status",
    tc_id="TC-28",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"youre_subscribed_message_visible": "true", "aspectproof_layout_issues_seen_this_session": "Issues seen this session: 0", "layout_report": "AspectProof layout\nTablet landscape 1024\u00d7768 (full window)\nProbe: active (67 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=tablet-landscape&run=r3-tablet-landscape__signup&start=%2F', instruction_id='21801fec-1ca7-4f86-bfa8-a0fbd04ac1f2'):
        await page.goto("http://localhost:4400/__ap/frame?profile=tablet-landscape&run=r3-tablet-landscape__signup&start=%2F")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Dismiss promotion button', instruction_id='c2b0663c-6c24-46b8-9eb3-83749b453b07'):
        _loc_2 = frame_0.locator("internal:role=button[name=\"Dismiss promotion\"i]")
        
        await _loc_2.click()
        # Reset to main page context
    
    async with testmu.step('Waiting for the queued plan to continue typing Name', instruction_id='07c4c41c-7c93-4fb1-9722-e1416d327401'):
        await page.wait_for_timeout(1000)
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "Test User" into "Name"', instruction_id='ae08f710-9956-441d-a963-a651b55da850'):
        element_0 = frame_2.locator("internal:role=textbox[name=\"Name\"i]")
        
        await testmu.fill(element_0, "Test User")
        # Reset to main page context
        frame_3 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "test@example.com" into "Email"', instruction_id='c49789ea-c53a-4d1b-afe9-77066fa833b3'):
        element_1 = frame_3.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_1, "test@example.com")
        # Reset to main page context
        frame_4 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Subscribe button in Get trail notes form', instruction_id='e3c289e5-131e-4a66-8b3a-8c1a58a19fdb'):
        _loc_6 = frame_4.locator("internal:role=button[name=\"Subscribe\"i]")
        
        await _loc_6.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the subscription confirmation message is present'):
        set_var('youre_subscribed_message_visible', await testmu.textual_analyzer(page, wrapped_js='(els) => {\n  const __m = {19: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(19).innerText.includes("You\'re subscribed"));\n  return (typeof __v === \'boolean\' ? String(__v) : __v);\n}', locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Thanks, Test User! You\'re"i'], query="whether a 'You're subscribed' message is present in the subscription form status message", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="a 'You're subscribed' message appears"))
    
    async with testmu.step('Reading the session issue count from the AspectProof layout panel'):
        set_var('aspectproof_layout_issues_seen_this_session', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {23: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(23).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Issues seen this session:"i'], query='the Issues seen this session value in the AspectProof layout panel', expected_value='Issues seen this session: 0', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the "AspectProof layout" panel shows "Issues seen this session: 0"'))
    
    async with testmu.step('Extracting the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {20: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(20).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full "AspectProof layout" panel text is saved as {{layout_report}}'))
    
    async with testmu.step('Assertion check', instruction_id='da6a7e2d-ab88-4897-ad5b-c6727fe80bf9'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "a 'You're subscribed' message appears", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{youre_subscribed_message_visible}}', 'store_key': 'youre_subscribed_message_visible', 'variable_refs': {'{{youre_subscribed_message_visible}}': 'true'}}], 'sub_checks': [{'description': "a 'You're subscribed' message appears", 'store_key': 'youre_subscribed_message_visible', 'expected_value': 'true', 'extracted_value': '{{youre_subscribed_message_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "a 'You're subscribed' message appears"})
    
    async with testmu.step('Assertion check', instruction_id='40bedd50-180e-4523-a87b-72fce59b466e'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'passed': True, 'operator': 'equals', 'transforms': ['strip'], 'json_path': None, 'expected': 'Issues seen this session: 0', 'extracted_value': '{{aspectproof_layout_issues_seen_this_session}}', 'store_key': 'aspectproof_layout_issues_seen_this_session', 'variable_refs': {'{{aspectproof_layout_issues_seen_this_session}}': 'Issues seen this session: 0'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'store_key': 'aspectproof_layout_issues_seen_this_session', 'expected_value': 'Issues seen this session: 0', 'extracted_value': '{{aspectproof_layout_issues_seen_this_session}}', 'operator': 'equals', 'transforms': ['strip']}], 'composite_operator': 'and', 'claim': 'the "AspectProof layout" panel shows "Issues seen this session: 0"'})


if __name__ == "__main__":
    testmu.run(test)