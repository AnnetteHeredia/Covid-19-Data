--
-- File generated with SQLiteStudio v3.3.3 on Tue Apr 12 21:14:54 2022
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: usa_data
CREATE TABLE usa_data (
    [submission_date
] DATE,
    [state
]           TEXT,
    [tot_cases
]       INTEGER,
    [conf_cases
]      INTEGER,
    [prob_cases
]      INTEGER,
    [new_case
]        INTEGER,
    [pnew_case
]       INTEGER,
    [tot_death
]       INTEGER,
    [conf_death
]      INTEGER,
    [prob_death
]      INTEGER,
    [new_death
]       INTEGER,
    [pnew_death
]      INTEGER,
    [created_at
]      DATETIME,
    [consent_cases
]   TEXT,
    [consent_deaths
]  TEXT
);


-- Table: world_data
CREATE TABLE world_data (
    [iso_code
]           TEXT,
    [continent
]          TEXT,
    [location
]           TEXT,
    [date
]               DATE,
    [total_cases
]        INTEGER,
    [new_cases
]          INTEGER,
    [total_deaths
]       INTEGER,
    [new_deaths
]         INTEGER,
    [reproduction_rate
]  DECIMAL,
    [icu_patients
]       INTEGER,
    [hosp_patients
]      INTEGER,
    [new_tests
]          INTEGER,
    [total_tests
]        INTEGER,
    [positive_rate
]      DECIMAL,
    [tests_units
]        INTEGER,
    [total_vaccinations
] INTEGER,
    [people_vaccinated
]  INTEGER,
    [new_vaccinations
]   INTEGER,
    [stringency_index
]   DECIMAL,
    [population
]         INTEGER,
    [population_density
] DECIMAL,
    [median_age
]         DECIMAL,
    [gdp_per_capita
]     DECIMAL
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
