import os.path

from selene import browser, be, have

def test_add_data_registration_and_submit(demo_qa):
    browser.element('.practice-form-wrapper').should(be.visible and have.text('Practice Form'))
    browser.element('#firstName').should(have.attribute('placeholder').value('First Name')).type('UserFirstName')
    browser.element('#lastName').should(have.attribute('placeholder').value('Last Name')).type('UserLastName')
    browser.element('#userEmail').should(have.attribute('placeholder').value('name@example.com')).type('test.email@gmail.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(have.attribute('placeholder').value('Mobile Number')).type('9992220000')
    browser.element('#dateOfBirthInput').should(be.visible).click()
    browser.element('.react-datepicker__month-select').should(be.visible).click()
    browser.element('option[value="4"]').click()
    browser.element('.react-datepicker__year-select').should(be.visible).click()
    browser.element('option[value="2000"]').click()
    browser.element('.react-datepicker__day--020').click()
    browser.element('#dateOfBirthInput').should(have.value('20 May 2000'))
    browser.element('#subjectsInput').set('Maths').press_enter()
    browser.element('#subjectsInput').set('Physics').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('test_picture.jpg'))
    browser.element('#currentAddress').should(have.attribute('placeholder').value('Current Address')).type('country city street house')
    # Выбор штата и города
    browser.element('#state').click()
    browser.element('#react-select-3-option-3').click() #setTimeout(function(){debugger; }, 5000)
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click() #setTimeout(function(){debugger; }, 5000)
    breakpoint()



