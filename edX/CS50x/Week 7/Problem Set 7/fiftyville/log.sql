-- Keep a log of any SQL queries you execute as you solve the mystery.

-- to see the description of the crime in the crime_scene_report table
SELECT description FROM crime_scene_reports WHERE street = "Humphrey Street" AND day = "28" AND month = "7" AND year = "2021";

-- theft of the cs50 duck took place on Humphrey Street on 28-july-2021 at 10:15.
-- 3 witness present at the time and mentions the bakery.

-- to see the name and transcript of the witness in the interviews table
SELECT name, transcript FROM interviews WHERE day = "28" AND month = "7" AND year = "2021";

-- Ruth : He said within 10 mins of the theft. Theif get into a car in the bakery parking lot and drive away.
    -- In the security footage of the bakery parking lot, look for the cars that left the parking lot in that time.
-- Eugene : He said, don't know the theif's name but he was someone i recognized. Early morning, before arriving to
    -- Emma's bakery, he was walking by the ATM on Leggett Street and saw the theif withdrawing money.
-- Raymond : He said, when theif was leaving bakery he was on a call with someone for less than a minute.
    -- He heard that they were planning to take the earliest flight out of fiftyville tomorrow. The theif asked the other
    -- person on call to purchase the flight ticket.

-- as mentioned by ruth checking the bakery_security_logs table and the people table for name and license_plate
-- so we have a list of suspects
SELECT * FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_securtiy_logs WHERE day = "28" AND month = "7"
AND year = "2021" AND hour = "10" AND minute >= "15" AND minute <= "25" AND activity = "exit");

-- as mentioned by eugene checking the atm_transactions table, the bank_accounts table and the people table
-- for account_number, person_id and name so we have one more suspect list
SELECT * FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM
atm_transactions WHERE day = "28" AND month = "7" AND year = "2021" AND atm_location = "Leggett Street" AND
transaction_type = "withdraw"));

-- Now from the 2 suspent list, we have 4 common names that are Iman, Luca, Diana and Bruce

-- as mentioned by raymond checking the phone_calls table and people table for phone_number and name
-- so we have one more suspect list
SELECT * FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE year = "2021" AND day = "28" AND month = "7"
AND duration <= "60");

-- Now from the 3 suspect list, we have 2 common names that are Diana, Bruce

-- as mentioned by raymond checking the flights table
SELECT flights.id, full_name, city, hour, minute FROM airports JOIN flights ON airports.id = flights.destination_airport_id
WHERE year = "2021" AND month = "7" AND day = "29" AND origin_airport_id = (SELECT id FROM airports WHERE
city = "Fiftyville") ORDER BY hour, minute;

-- the earliest flight id is 36 and is at 8:20 to New York City and the airport is LAGuardia Airport

-- we got a new suspect list
SELECT * FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id IN (SELECT destination_airport_id FROM flights WHERE year = "2021" AND month = "7"
AND day = "29" AND hour = "8" AND minute = "20"));

-- From the short listed suspect list the name which is common is Bruce.
SELECT * FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE year = "2021" AND month = "7" AND
day = "28" AND duration <= "60" AND caller = "(367) 555-5533");


-- Accordind to my research, Bruce is the theif who went to New York city and his accomplice is Robin wo helped him escape