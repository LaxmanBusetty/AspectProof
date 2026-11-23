import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="4d2281f3-3a29-485d-8e95-cd7fbd62fb3c",
    name="Subscribe to Trail Notes and Verify Layout Status",
    tc_id="TC-7",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"subscribed_message_appears": "true", "layout_issues_seen_this_session": "0", "layout_report": "AspectProof layout\nDesktop 1920\u00d71080 (full window)\nProbe: active (70 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=desktop-1920&run=r3-desktop-1920__signup&start=%2F', instruction_id='c7d87f50-9fe8-422e-8e81-a0b88c13b344'):
        await page.goto("http://localhost:4400/__ap/frame?profile=desktop-1920&run=r3-desktop-1920__signup&start=%2F")
    
    async with testmu.step('Waiting for the plan to start', instruction_id='cb2edbad-ce52-4fc6-bd71-dc513fa3f443'):
        await page.wait_for_timeout(1000)
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "Test User" into "Name"', instruction_id='f4c3bb4b-bdb8-4628-9d76-3f72227d26be'):
        element_0 = frame_0.locator("internal:role=textbox[name=\"Name\"i]")
        
        await testmu.fill(element_0, "Test User")
        # Reset to main page context
        frame_1 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "test@example.com" into "Email"', instruction_id='a759d637-32b9-4a30-86f7-2b2cbdc0a054'):
        element_1 = frame_1.locator("internal:role=textbox[name=\"Email\"i]")
        
        await testmu.fill(element_1, "test@example.com")
        # Reset to main page context
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Subscribe button', instruction_id='ef25a58d-37de-4c37-9c2b-9d84cf2ccd71'):
        _loc_4 = frame_2.locator("internal:role=button[name=\"Subscribe\"i]")
        
        await _loc_4.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the subscription confirmation message is present'):
        set_var('subscribed_message_appears', await testmu.textual_analyzer(page, wrapped_js='(els) => {\n  const __m = {23: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(23).innerText.includes("You\'re subscribed"));\n  return (typeof __v === \'boolean\' ? String(__v) : __v);\n}', locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Thanks, Test User! You\'re"i'], query="whether a 'You're subscribed' message is present in the subscription form status", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="a 'You're subscribed' message appears"))
    
    async with testmu.step('Assertion check', instruction_id='f217810f-37ae-436c-8826-76c8e86376c1'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "a 'You're subscribed' message appears", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{subscribed_message_appears}}', 'store_key': 'subscribed_message_appears', 'variable_refs': {'{{subscribed_message_appears}}': 'true'}}], 'sub_checks': [{'description': "a 'You're subscribed' message appears", 'store_key': 'subscribed_message_appears', 'expected_value': 'true', 'extracted_value': '{{subscribed_message_appears}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "a 'You're subscribed' message appears"})
    
    async with testmu.step('Reading the session layout issue count'):
        set_var('layout_issues_seen_this_session', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {31: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(31).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['#ap-seen'], query='the issue count shown after "Issues seen this session:" in the AspectProof layout panel', expected_value='0', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the "AspectProof layout" panel shows "Issues seen this session: 0"'))
    
    async with testmu.step('Extracting the AspectProof layout panel report'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {27: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(27).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full "AspectProof layout" panel text is stored as {{layout_report}}'))
    
    async with testmu.step('Assertion check', instruction_id='1b83db2a-6efb-4a7f-925a-eb479ecc6ffe'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'passed': True, 'operator': 'equals', 'transforms': ['strip'], 'json_path': None, 'expected': '0', 'extracted_value': '{{layout_issues_seen_this_session}}', 'store_key': 'layout_issues_seen_this_session', 'variable_refs': {'{{layout_issues_seen_this_session}}': '0'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'store_key': 'layout_issues_seen_this_session', 'expected_value': '0', 'extracted_value': '{{layout_issues_seen_this_session}}', 'operator': 'equals', 'transforms': ['strip']}], 'composite_operator': 'and', 'claim': 'the "AspectProof layout" panel shows "Issues seen this session: 0"'})


if __name__ == "__main__":
    testmu.run(test)