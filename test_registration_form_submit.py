import os.path
from selene import browser, be, have

def test_add_data_registration_and_submit(demo_qa):
    # Check if the practice form is visible and has the correct text
    browser.element('.practice-form-wrapper').should(be.visible and have.text('Practice Form'))

    # Fill in the form fields
    browser.element('#firstName').should(have.attribute('placeholder').value('First Name')).type('UserFirstName')
    browser.element('#lastName').should(have.attribute('placeholder').value('Last Name')).type('UserLastName')
    browser.element('#userEmail').should(have.attribute('placeholder').value('name@example.com')).type('test.email@gmail.com')

    # Select the male gender
    browser.element('label[for="gender-radio-1"]').click()

    # Fill in the mobile number field
    browser.element('#userNumber').should(have.attribute('placeholder').value('Mobile Number')).type('9992220000')

    # Set the date of birth
    browser.element('#dateOfBirthInput').should(be.visible).click()
    browser.element('.react-datepicker__month-select').should(be.visible).click()
    browser.element('option[value="4"]').click()
    browser.element('.react-datepicker__year-select').should(be.visible).click()
    browser.element('option[value="2000"]').click()
    browser.element('.react-datepicker__day--020').click()
    browser.element('#dateOfBirthInput').should(have.value('20 May 2000')) # check date

    # Select subjects
    browser.element('#subjectsInput').set('Maths').press_enter()
    browser.element('#subjectsInput').set('Physics').press_enter()

    # Select the hobby "Sports"
    browser.element('label[for="hobbies-checkbox-1"]').click()

    # Upload a picture
    browser.element('#uploadPicture').send_keys(os.path.abspath('test_picture.jpg'))

    # Fill in the current address field
    browser.element('#currentAddress').should(have.attribute('placeholder').value('Current Address')).type('country city street house')

    # Select the state and city (setTimeout(function(){debugger; }, 5000))
    browser.element('#state').click()
    browser.element('#react-select-3-option-3').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

    # Submit the form
    browser.element('#submit').should(be.visible and be.clickable and be.enabled).click()

    # Finish check URL, the modal title, values and close button
    browser.should(have.url('https://demoqa.com/automation-practice-form/'))
    browser.element('#example-modal-sizes-title-lg').should(be.visible).should(have.exact_text('Thanks for submitting the form'))
    #breakpoint()

    browser.element('.modal-body').all('tr').should(have.exact_texts
        (
            'Label Values',
            'Student Name UserFirstName UserLastName',
            'Student Email test.email@gmail.com',
            'Gender Male',
            'Mobile 9992220000',
            'Date of Birth 20 May,2000',
            'Subjects Maths, Physics',
            'Hobbies Sports',
            'Picture test_picture.jpg',
            'Address country city street house',
            'State and City Rajasthan Jaipur',

        )
    )

    browser.element('#closeLargeModal').should(be.clickable).should(have.text('Close'))




