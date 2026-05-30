# Database Knowledge Base

Generated on: In Progress
Total Tables: 89
Total Relationships: 6

# Tables


## USER

The primary business purpose of this database table would be to store user data, where each row represents a unique user entity characterized by their identity (entity.Identity), display name, current status (Active/Inactive), and timestamp records for tracking creation and last modification.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | Yes | No |
| display_name | VARCHAR(1024) | No | No |
| is_active | CHAR(1) | No | No |
| create_timestamp | TIMESTAMP | No | No |
| update_timestamp | TIMESTAMP | No | Yes |


## USER

The primary business purpose of this database table would be to store user data, where each row represents a unique user entity characterized by their identity (entity.Identity), display name, current status (Active/Inactive), and timestamp records for tracking creation and last modification.


## activity

The business purpose of a 'activity' database table is to store records of past or ongoing events (or activities) related to various entities, capturing key details about the activity, such as its nature, duration, and timestamp, for potential analysis, reporting, or auditing purposes.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | Yes | No |
| data | BLOB | No | Yes |
| details | NCLOB | No | Yes |
| name | VARCHAR(64) | No | No |
| type | VARCHAR(32) | No | No |
| status | VARCHAR(16) | No | No |
| started_timestamp | TIMESTAMP | No | No |
| ended_timestamp | TIMESTAMP | No | Yes |
| create_timestamp | TIMESTAMP | No | No |
| update_timestamp | TIMESTAMP | No | Yes |


## activity

The business purpose of a 'activity' database table is to store records of past or ongoing events (or activities) related to various entities, capturing key details about the activity, such as its nature, duration, and timestamp, for potential analysis, reporting, or auditing purposes.


## address

The business purpose of a database table named 'address' with the listed columns is likely to store and manage geographic residence information for entities, customers, or individuals, providing a structured way to capture and organize address details.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | Yes | No |
| checksum | VARCHAR(32) | No | Yes |
| status | VARCHAR(32) | No | No |
| source_name | VARCHAR(32) | No | No |
| source_reference | VARCHAR(64) | No | Yes |
| purpose_code | VARCHAR(32) | No | Yes |
| purpose_name | VARCHAR(256) | No | Yes |
| country_code | VARCHAR(32) | No | Yes |
| country_name | VARCHAR(256) | No | Yes |
| state_code | VARCHAR(32) | No | Yes |
| state_name | VARCHAR(256) | No | Yes |
| province_code | VARCHAR(32) | No | Yes |
| province_name | VARCHAR(256) | No | Yes |
| municipality_code | VARCHAR(32) | No | Yes |
| municipality_name | VARCHAR(256) | No | Yes |
| city_code | VARCHAR(32) | No | Yes |
| city_name | VARCHAR(256) | No | Yes |
| district_code | VARCHAR(32) | No | Yes |
| district_name | VARCHAR(256) | No | Yes |
| street_code | VARCHAR(32) | No | Yes |
| street_name | VARCHAR(256) | No | Yes |
| street_number | NUMBER | No | Yes |
| street_type | VARCHAR(256) | No | Yes |
| floor_code | VARCHAR(32) | No | Yes |
| floor_name | VARCHAR(256) | No | Yes |
| floor_number | NUMBER | No | Yes |
| room_code | VARCHAR(32) | No | Yes |
| room_name | VARCHAR(256) | No | Yes |
| room_number | NUMBER | No | Yes |
| door_code | VARCHAR(32) | No | Yes |
| door_name | VARCHAR(256) | No | Yes |
| door_number | NUMBER | No | Yes |
| door_letter | VARCHAR(16) | No | Yes |
| door_prefix | VARCHAR(16) | No | Yes |
| door_suffix | VARCHAR(16) | No | Yes |
| door_type | VARCHAR(256) | No | Yes |
| postal_box | VARCHAR(16) | No | Yes |
| postal_code | VARCHAR(16) | No | Yes |
| boundary | NULL | No | Yes |
| location | NULL | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| valid_to | TIMESTAMP | No | Yes |
| create_timestamp | TIMESTAMP | No | No |
| update_timestamp | TIMESTAMP | No | Yes |
| fullmatch_key | VARCHAR(512) | No | No |
| paid | VARCHAR(24) | No | No |
| is_leading | NUMBER | No | No |
| validity | VARCHAR(32) | No | No |


## address

The business purpose of a database table named 'address' with the listed columns is likely to store and manage geographic residence information for entities, customers, or individuals, providing a structured way to capture and organize address details.


## address_attribute

The business purpose of a database table named 'address_attribute' appears to be storing attributes related to geographical locations or addresses, such as attributes like the country, city, or postal code, where each row likely represents an attribute with its respective value and timestamp.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | Yes | No |
| parent_identity | VARCHAR(36) | No | No |
| name | VARCHAR(32) | No | No |
| type | VARCHAR(16) | No | No |
| value_point | NULL | No | Yes |
| value_polygon | NULL | No | Yes |
| value_number | NUMBER | No | Yes |
| value_string | VARCHAR(1024) | No | Yes |
| create_timestamp | TIMESTAMP | No | No |
| update_timestamp | TIMESTAMP | No | Yes |


## address_attribute

The business purpose of a database table named 'address_attribute' appears to be storing attributes related to geographical locations or addresses, such as attributes like the country, city, or postal code, where each row likely represents an attribute with its respective value and timestamp.


## address_attribute_pre30

The business purpose of this database table appears to be storing geospatial attribute data for postal addresses collected before December 30th, likely as part of a spatial reference system or mapping application.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | No |
| parent_identity | VARCHAR(36) | No | No |
| name | VARCHAR(32) | No | No |
| type | VARCHAR(16) | No | No |
| value_point | NULL | No | Yes |
| value_polygon | NULL | No | Yes |
| value_number | NUMBER | No | Yes |
| value_string | VARCHAR(1024) | No | Yes |
| create_timestamp | TIMESTAMP | No | No |
| update_timestamp | TIMESTAMP | No | Yes |


## address_attribute_pre30

The business purpose of this database table appears to be storing geospatial attribute data for postal addresses collected before December 30th, likely as part of a spatial reference system or mapping application.


## address_attribute_restore

The business purpose of a database table named 'address_attribute_restore' appears to be to store historical restore point values for address attributes that can change over time, allowing for the retrieval and recovery of previous attribute values when needed.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | Yes |
| parent_identity | VARCHAR(36) | No | Yes |
| name | VARCHAR(32) | No | Yes |
| type | VARCHAR(16) | No | Yes |
| value_point | NULL | No | Yes |
| value_polygon | NULL | No | Yes |
| value_number | NUMBER | No | Yes |
| value_string | VARCHAR(1024) | No | Yes |
| create_timestamp | TIMESTAMP | No | Yes |
| update_timestamp | TIMESTAMP | No | Yes |


## address_attribute_restore

The business purpose of a database table named 'address_attribute_restore' appears to be to store historical restore point values for address attributes that can change over time, allowing for the retrieval and recovery of previous attribute values when needed.


## address_diagnostic

The business purpose of the "address_diagnostic" database table appears to be storing diagnostic information related to entities (e.g., patients, customers) located at specific addresses, with relevant details such as address codes, descriptions, and corresponding severity levels.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | Yes | No |
| parent_identity | VARCHAR(36) | No | No |
| code | VARCHAR(16) | No | No |
| description | VARCHAR(1024) | No | Yes |
| severity | VARCHAR(16) | No | No |
| create_timestamp | TIMESTAMP | No | No |
| update_timestamp | TIMESTAMP | No | Yes |


## address_diagnostic

The business purpose of the "address_diagnostic" database table appears to be storing diagnostic information related to entities (e.g., patients, customers) located at specific addresses, with relevant details such as address codes, descriptions, and corresponding severity levels.


## address_diagnostic_restore

The database table 'address_diagnostic_restore' seems to track diagnostic restore data for addresses, storing information such as entity identity, parent identity, diagnosis codes, descriptions, and timestamps, suggesting it is used in a healthcare or insurance setting to monitor and manage the restoration of addressed entities, likely using a normalization process.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | Yes |
| parent_identity | VARCHAR(36) | No | Yes |
| code | VARCHAR(16) | No | Yes |
| description | VARCHAR(1024) | No | Yes |
| severity | VARCHAR(16) | No | Yes |
| create_timestamp | TIMESTAMP | No | Yes |
| update_timestamp | TIMESTAMP | No | Yes |


## address_diagnostic_restore

The database table 'address_diagnostic_restore' seems to track diagnostic restore data for addresses, storing information such as entity identity, parent identity, diagnosis codes, descriptions, and timestamps, suggesting it is used in a healthcare or insurance setting to monitor and manage the restoration of addressed entities, likely using a normalization process.


## address_event

The database table 'address_event' likely stores events related to changes or updates to entities (e.g., users, organizations) and their associated addresses, with each record capturing the context of a specific change, such as an address update for a user.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | Yes | No |
| parent_identity | VARCHAR(36) | No | No |
| message | VARCHAR(1024) | No | Yes |
| type | VARCHAR(16) | No | No |
| user_identity | VARCHAR(36) | No | No |
| create_timestamp | TIMESTAMP | No | No |
| update_timestamp | TIMESTAMP | No | Yes |


## address_event

The database table 'address_event' likely stores events related to changes or updates to entities (e.g., users, organizations) and their associated addresses, with each record capturing the context of a specific change, such as an address update for a user.


## address_event_restore

The business purpose of a 'address_event_restore' database table appears to be storing audit trail or event log entries related to updates or changes made to physical addresses, likely in the context of property management or customer information systems.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | Yes |
| parent_identity | VARCHAR(36) | No | Yes |
| message | VARCHAR(1024) | No | Yes |
| type | VARCHAR(16) | No | Yes |
| user_identity | VARCHAR(36) | No | Yes |
| create_timestamp | TIMESTAMP | No | Yes |
| update_timestamp | TIMESTAMP | No | Yes |


## address_event_restore

The business purpose of a 'address_event_restore' database table appears to be storing audit trail or event log entries related to updates or changes made to physical addresses, likely in the context of property management or customer information systems.


## address_pre30

The 'address_pre30' database table appears to be storing pre-2010 version of addresses in a standardized format, likely for business or organizational use, such as customer data or geographic location information.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | No |
| checksum | VARCHAR(32) | No | Yes |
| status | VARCHAR(32) | No | No |
| source_name | VARCHAR(32) | No | No |
| source_reference | VARCHAR(64) | No | Yes |
| purpose_code | VARCHAR(32) | No | Yes |
| purpose_name | VARCHAR(256) | No | Yes |
| country_code | VARCHAR(32) | No | Yes |
| country_name | VARCHAR(256) | No | Yes |
| state_code | VARCHAR(32) | No | Yes |
| state_name | VARCHAR(256) | No | Yes |
| province_code | VARCHAR(32) | No | Yes |
| province_name | VARCHAR(256) | No | Yes |
| municipality_code | VARCHAR(32) | No | Yes |
| municipality_name | VARCHAR(256) | No | Yes |
| city_code | VARCHAR(32) | No | Yes |
| city_name | VARCHAR(256) | No | Yes |
| district_code | VARCHAR(32) | No | Yes |
| district_name | VARCHAR(256) | No | Yes |
| street_code | VARCHAR(32) | No | Yes |
| street_name | VARCHAR(256) | No | Yes |
| street_number | NUMBER | No | Yes |
| street_type | VARCHAR(256) | No | Yes |
| floor_code | VARCHAR(32) | No | Yes |
| floor_name | VARCHAR(256) | No | Yes |
| floor_number | NUMBER | No | Yes |
| room_code | VARCHAR(32) | No | Yes |
| room_name | VARCHAR(256) | No | Yes |
| room_number | NUMBER | No | Yes |
| door_code | VARCHAR(32) | No | Yes |
| door_name | VARCHAR(256) | No | Yes |
| door_number | NUMBER | No | Yes |
| door_letter | VARCHAR(16) | No | Yes |
| door_prefix | VARCHAR(16) | No | Yes |
| door_suffix | VARCHAR(16) | No | Yes |
| door_type | VARCHAR(256) | No | Yes |
| postal_box | VARCHAR(16) | No | Yes |
| postal_code | VARCHAR(16) | No | Yes |
| boundary | NULL | No | Yes |
| location | NULL | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| valid_to | TIMESTAMP | No | Yes |
| create_timestamp | TIMESTAMP | No | No |
| update_timestamp | TIMESTAMP | No | Yes |


## address_pre30

The 'address_pre30' database table appears to be storing pre-2010 version of addresses in a standardized format, likely for business or organizational use, such as customer data or geographic location information.


## address_relation

The business purpose of a database table named 'address_relation' appears to be tracking relationships between entities related to addresses, such as mapping an individual's address to their profile or identifying corresponding shipping and billing addresses.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | Yes | No |
| source_identity | VARCHAR(36) | No | No |
| target_identity | VARCHAR(36) | No | No |
| type | VARCHAR(32) | No | No |
| create_timestamp | TIMESTAMP | No | No |
| update_timestamp | TIMESTAMP | No | Yes |


## address_relation

The business purpose of a database table named 'address_relation' appears to be tracking relationships between entities related to addresses, such as mapping an individual's address to their profile or identifying corresponding shipping and billing addresses.


## address_relation_restore

The business purpose of a database table named 'address_relation_restore' appears to be storing historical relationships and restorative data related to address book or directory management, likely retaining records from past updates or merges.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | Yes |
| source_identity | VARCHAR(36) | No | Yes |
| target_identity | VARCHAR(36) | No | Yes |
| type | VARCHAR(32) | No | Yes |
| create_timestamp | TIMESTAMP | No | Yes |
| update_timestamp | TIMESTAMP | No | Yes |


## address_relation_restore

The business purpose of a database table named 'address_relation_restore' appears to be storing historical relationships and restorative data related to address book or directory management, likely retaining records from past updates or merges.


## address_restore

The business purpose of a database table named 'address_restore' appears to be storing and managing corrected or restored addresses across various entities, with each record representing a unique address that has undergone changes, adjustments, or corrections.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | Yes |
| checksum | VARCHAR(32) | No | Yes |
| status | VARCHAR(32) | No | Yes |
| source_name | VARCHAR(32) | No | Yes |
| source_reference | VARCHAR(64) | No | Yes |
| purpose_code | VARCHAR(32) | No | Yes |
| purpose_name | VARCHAR(256) | No | Yes |
| country_code | VARCHAR(32) | No | Yes |
| country_name | VARCHAR(256) | No | Yes |
| state_code | VARCHAR(32) | No | Yes |
| state_name | VARCHAR(256) | No | Yes |
| province_code | VARCHAR(32) | No | Yes |
| province_name | VARCHAR(256) | No | Yes |
| municipality_code | VARCHAR(32) | No | Yes |
| municipality_name | VARCHAR(256) | No | Yes |
| city_code | VARCHAR(32) | No | Yes |
| city_name | VARCHAR(256) | No | Yes |
| district_code | VARCHAR(32) | No | Yes |
| district_name | VARCHAR(256) | No | Yes |
| street_code | VARCHAR(32) | No | Yes |
| street_name | VARCHAR(256) | No | Yes |
| street_number | NUMBER | No | Yes |
| street_type | VARCHAR(256) | No | Yes |
| floor_code | VARCHAR(32) | No | Yes |
| floor_name | VARCHAR(256) | No | Yes |
| floor_number | NUMBER | No | Yes |
| room_code | VARCHAR(32) | No | Yes |
| room_name | VARCHAR(256) | No | Yes |
| room_number | NUMBER | No | Yes |
| door_code | VARCHAR(32) | No | Yes |
| door_name | VARCHAR(256) | No | Yes |
| door_number | NUMBER | No | Yes |
| door_letter | VARCHAR(16) | No | Yes |
| door_prefix | VARCHAR(16) | No | Yes |
| door_suffix | VARCHAR(16) | No | Yes |
| door_type | VARCHAR(256) | No | Yes |
| postal_box | VARCHAR(16) | No | Yes |
| postal_code | VARCHAR(16) | No | Yes |
| boundary | NULL | No | Yes |
| location | NULL | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| valid_to | TIMESTAMP | No | Yes |
| create_timestamp | TIMESTAMP | No | Yes |
| update_timestamp | TIMESTAMP | No | Yes |


## address_restore

The business purpose of a database table named 'address_restore' appears to be storing and managing corrected or restored addresses across various entities, with each record representing a unique address that has undergone changes, adjustments, or corrections.


## adp30_upgrade_info

The business purpose of a database table named 'adp30_upgrade_info' with columns 'name' and 'value' is to store metadata or settings related to an upgrade process for an application or software version, such as configuration values or flags.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| name | VARCHAR(32) | No | Yes |
| value | VARCHAR(256) | No | Yes |


## adp30_upgrade_info

The business purpose of a database table named 'adp30_upgrade_info' with columns 'name' and 'value' is to store metadata or settings related to an upgrade process for an application or software version, such as configuration values or flags.


## anotherproblem

The business purpose of a database table named 'anothertest' would be to store test results or data related specifically by this name.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| column1 | VARCHAR(26) | No | Yes |


## anotherproblem

The business purpose of a database table named 'anothertest' would be to store test results or data related specifically by this name.


## application

The primary business purpose of this database table appears to be storing metadata for multiple applications, including their operational configuration through attributes like activation status, observation settings, and retry limits.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| code | VARCHAR(8) | Yes | No |
| description | VARCHAR(64) | No | Yes |
| status_attribute_name | VARCHAR(32) | No | Yes |
| is_active | CHAR(1) | No | No |
| operation_attribute_name | VARCHAR(32) | No | No |
| is_observer | CHAR(1) | No | No |
| retry_count_attribute_name | VARCHAR(32) | No | Yes |
| retry_limit | NUMBER | No | No |


## application

The primary business purpose of this database table appears to be storing metadata for multiple applications, including their operational configuration through attributes like activation status, observation settings, and retry limits.


## bag_update_0100

The business purpose of the 'bag_update_0100' database table appears to be tracking and updating entities, specifically geographical features such as municipalities, cities, and addresses, with associated predecessor and successor relationships, across different locations and valid periods.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | No |
| entity_identity_predecessor_old | VARCHAR(4000) | No | Yes |
| entity_identity_predecessor_new | VARCHAR(4000) | No | Yes |
| entity_identity_successor_old | VARCHAR(4000) | No | Yes |
| entity_identity_successor_new | VARCHAR(4000) | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| source_reference | VARCHAR(64) | No | Yes |
| municipality_name | VARCHAR(256) | No | Yes |
| city_name | VARCHAR(256) | No | Yes |
| street_name | VARCHAR(256) | No | Yes |
| postal_code | VARCHAR(1024) | No | Yes |
| door_number | NUMBER | No | Yes |
| door_letter | VARCHAR(16) | No | Yes |
| door_suffix | VARCHAR(16) | No | Yes |


## bag_update_0100

The business purpose of the 'bag_update_0100' database table appears to be tracking and updating entities, specifically geographical features such as municipalities, cities, and addresses, with associated predecessor and successor relationships, across different locations and valid periods.


## bag_update_0200

The business purpose of the database table 'bag_update_0200' appears to be storing information about updates made to building data entities at a specific point in time (indicated by the date in the column names), specifically tracking changes related to entity identity, local authority information (municipality and city), address details, and status updates.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | No |
| entity_identity_predecessor | VARCHAR(36) | No | Yes |
| entity_identity_successor | VARCHAR(36) | No | Yes |
| source_reference | VARCHAR(64) | No | Yes |
| status_old | VARCHAR(32) | No | No |
| status_new | VARCHAR(32) | No | Yes |
| status_predecessor | VARCHAR(32) | No | Yes |
| municipality_name | VARCHAR(256) | No | Yes |
| city_name | VARCHAR(256) | No | Yes |
| street_name | VARCHAR(256) | No | Yes |
| postal_code | VARCHAR(1024) | No | Yes |
| door_number | NUMBER | No | Yes |
| door_letter | VARCHAR(16) | No | Yes |
| door_suffix | VARCHAR(16) | No | Yes |


## bag_update_0200

The business purpose of the database table 'bag_update_0200' appears to be storing information about updates made to building data entities at a specific point in time (indicated by the date in the column names), specifically tracking changes related to entity identity, local authority information (municipality and city), address details, and status updates.


## bag_update_0300

The business purpose of a database table named 'bag_update_0300' with columns 'entity_identity' and 'entity_identity_predecessor' appears to be tracking changes in entity identities over time, likely for auditing or version control purposes.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | Yes |
| entity_identity_predecessor | VARCHAR(36) | No | Yes |


## bag_update_0300

The business purpose of a database table named 'bag_update_0300' with columns 'entity_identity' and 'entity_identity_predecessor' appears to be tracking changes in entity identities over time, likely for auditing or version control purposes.


## bag_update_0400

The business purpose of a database table named 'bag_update_0400' is to store updates or changes related to entities (e.g. organizations, projects, etc.) at 4:00 PM that have occurred between the MoA (Master of Agreement) and "status" levels within an organization.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | No |
| entity_identity_moa | VARCHAR(36) | No | No |
| entity_identity_divisions | VARCHAR(4000) | No | Yes |
| entity_identity_retire | VARCHAR(36) | No | Yes |
| status | VARCHAR(32) | No | No |
| status_moa | VARCHAR(32) | No | No |
| paid | VARCHAR(1024) | No | Yes |
| paid_moa | VARCHAR(1024) | No | Yes |


## bag_update_0400

The business purpose of a database table named 'bag_update_0400' is to store updates or changes related to entities (e.g. organizations, projects, etc.) at 4:00 PM that have occurred between the MoA (Master of Agreement) and "status" levels within an organization.


## bag_update_0500

The business purpose of the 'bag_update_0500' database table appears to be a data warehouse or reporting staging area for collecting and organizing update-related information about various municipal locations (e.g., addresses), likely used for auditing, tracking changes, and facilitating data exchange between internal systems or external stakeholders.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | No |
| entity_identity_divisions | VARCHAR(4000) | No | Yes |
| entity_identity_predecessors | VARCHAR(4000) | No | Yes |
| source_name | VARCHAR(32) | No | No |
| source_reference | VARCHAR(64) | No | Yes |
| status | VARCHAR(32) | No | No |
| status_next | VARCHAR(32) | No | Yes |
| diagnostic_codes | VARCHAR(4000) | No | Yes |
| diagnostic_descriptions | VARCHAR(4000) | No | Yes |
| diagnostic_severities | VARCHAR(4000) | No | Yes |
| municipality_name | VARCHAR(256) | No | Yes |
| city_name | VARCHAR(256) | No | Yes |
| street_name | VARCHAR(256) | No | Yes |
| postal_code | VARCHAR(1024) | No | Yes |
| door_number | NUMBER | No | Yes |
| door_letter | VARCHAR(16) | No | Yes |
| door_suffix | VARCHAR(16) | No | Yes |


## bag_update_0500

The business purpose of the 'bag_update_0500' database table appears to be a data warehouse or reporting staging area for collecting and organizing update-related information about various municipal locations (e.g., addresses), likely used for auditing, tracking changes, and facilitating data exchange between internal systems or external stakeholders.


## bag_update_0600

The business purpose of a database table named 'bag_update_0600' with columns 'entity_identity', 'attribute_names', and 'diagnostic_codes' is likely to track and update attributes or symptoms (diagnostic codes) associated with specific entities (e.g., patients, products, assets), possibly in a systematic or routine manner.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | Yes |
| attribute_names | VARCHAR(4000) | No | Yes |
| diagnostic_codes | VARCHAR(4000) | No | Yes |


## bag_update_0600

The business purpose of a database table named 'bag_update_0600' with columns 'entity_identity', 'attribute_names', and 'diagnostic_codes' is likely to track and update attributes or symptoms (diagnostic codes) associated with specific entities (e.g., patients, products, assets), possibly in a systematic or routine manner.


## bag_update_0700

The primary business purpose of a database table named 'bag_update_0700' with those columns is to track updates related to bags held by a system or organization at 7am (0700), likely used for inventory management or logistics purposes.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | Yes |
| source_name | VARCHAR(32) | No | Yes |
| status | VARCHAR(32) | No | Yes |
| status_holding | VARCHAR(128) | No | Yes |
| status_pending | VARCHAR(128) | No | Yes |


## bag_update_0700

The primary business purpose of a database table named 'bag_update_0700' with those columns is to track updates related to bags held by a system or organization at 7am (0700), likely used for inventory management or logistics purposes.


## bag_update_blacklist

The business purpose of 'bag_update_blacklist' appears to be tracking and identifying outdated or problematic sources associated with bags for updates to prevent any negative impacts.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| source_reference | VARCHAR(16) | No | Yes |


## bag_update_blacklist

The business purpose of 'bag_update_blacklist' appears to be tracking and identifying outdated or problematic sources associated with bags for updates to prevent any negative impacts.


## cleaning_ap_0000_publication_attribute

The business purpose of the database table 'cleaning_ap_0000_publication_attribute' appears to be managing publication attributes for academic institutions, likely related to funding or research initiatives, and storing relevant details such as entity ID, payment information, source name, status, and applicable attributes and values.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | Yes |
| paid | VARCHAR(16) | No | Yes |
| source_name | VARCHAR(16) | No | Yes |
| status | VARCHAR(16) | No | Yes |
| attribute_name | VARCHAR(16) | No | Yes |
| attribute_value | VARCHAR(16) | No | Yes |


## cleaning_ap_0000_publication_attribute

The business purpose of the database table 'cleaning_ap_0000_publication_attribute' appears to be managing publication attributes for academic institutions, likely related to funding or research initiatives, and storing relevant details such as entity ID, payment information, source name, status, and applicable attributes and values.


## cleaning_ap_0100_postal_code_tmp

The business purpose of such a database table would be to store temporary postal code data for cleaning and validation purposes for addresses or entities (referred to as "entity_identity") associated with the primary table, likely in preparation for further processing or cleansing.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| row | ROWID | No | Yes |
| entity_identity | VARCHAR(36) | No | Yes |


## cleaning_ap_0100_postal_code_tmp

The business purpose of such a database table would be to store temporary postal code data for cleaning and validation purposes for addresses or entities (referred to as "entity_identity") associated with the primary table, likely in preparation for further processing or cleansing.


## cleaning_ap_1c_active

The business purpose of a database table named 'cleaning_ap_1c_active' with columns `entity_identity`, `paid`, and `status` is to store information about actively cleaning accounts in the 1c accounting system.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | Yes |
| paid | VARCHAR(16) | No | Yes |
| status | VARCHAR(16) | No | Yes |


## cleaning_ap_1c_active

The business purpose of a database table named 'cleaning_ap_1c_active' with columns `entity_identity`, `paid`, and `status` is to store information about actively cleaning accounts in the 1c accounting system.


## cleaning_ap_1g_active

The business purpose of the 'cleaning_ap_1g_active' database table appears to be a data cleansing and validation process for ActivePass project 1G, likely related to payment processing or billing management.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | Yes |
| status | VARCHAR(16) | No | Yes |
| paid | VARCHAR(16) | No | Yes |
| paid_orca | VARCHAR(16) | No | Yes |
| paid_oss10 | VARCHAR(16) | No | Yes |
| paid_pni | VARCHAR(16) | No | Yes |
| status_orca | VARCHAR(16) | No | Yes |
| status_oss10 | VARCHAR(16) | No | Yes |
| status_pni | VARCHAR(16) | No | Yes |


## cleaning_ap_1g_active

The business purpose of the 'cleaning_ap_1g_active' database table appears to be a data cleansing and validation process for ActivePass project 1G, likely related to payment processing or billing management.


## cleaning_ap_9_street_name_short

The business purpose of a database table 'cleaning_ap_9_street_name_short' is to store and manage a list of abbreviations for street names in a specific apartment complex (identified by the 'entity_identity' column), likely used for mapping and cleaning purposes.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | Yes |


## cleaning_ap_9_street_name_short

The business purpose of a database table 'cleaning_ap_9_street_name_short' is to store and manage a list of abbreviations for street names in a specific apartment complex (identified by the 'entity_identity' column), likely used for mapping and cleaning purposes.


## cleanup_address

The business purpose of a database table named 'cleanup_address' with the column 'source_reference' suggests that it is used to store a clean and unified version of customer addresses associated with their identifying reference from outside sources or external data providers.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| source_reference | VARCHAR(20) | No | Yes |


## cleanup_address

The business purpose of a database table named 'cleanup_address' with the column 'source_reference' suggests that it is used to store a clean and unified version of customer addresses associated with their identifying reference from outside sources or external data providers.


## cleanup_address_entity

The business purpose of a database table named 'cleanup_address_entity' appears to be tracking and managing accurate address data by storing information on entities that require cleanup or cleansing, along with their associated sources, status, and validation history.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| source_reference | VARCHAR(20) | No | Yes |
| entity_identity | VARCHAR(36) | No | Yes |
| source_name | VARCHAR(5) | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| status | VARCHAR(32) | No | Yes |
| full_match_string | VARCHAR(256) | No | Yes |
| version_from_latest | INTEGER | No | Yes |


## cleanup_address_entity

The business purpose of a database table named 'cleanup_address_entity' appears to be tracking and managing accurate address data by storing information on entities that require cleanup or cleansing, along with their associated sources, status, and validation history.


## cleanup_address_entity_0h1

The business purpose of a database table named 'cleanup_address_entity_0h1' appears to be storing and managing pre-processed address data by comparing it against a "latest" version or source (as indicated by columns indicating both original and corrected data), likely for use in cleansing, validating, or updating address records.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| source_reference | VARCHAR(20) | No | Yes |
| entity_identity | VARCHAR(36) | No | Yes |
| paid | VARCHAR(20) | No | Yes |
| source_name | VARCHAR(5) | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| status | VARCHAR(32) | No | Yes |
| full_match_string | VARCHAR(256) | No | Yes |
| version_from_latest | INTEGER | No | Yes |


## cleanup_address_entity_0h1

The business purpose of a database table named 'cleanup_address_entity_0h1' appears to be storing and managing pre-processed address data by comparing it against a "latest" version or source (as indicated by columns indicating both original and corrected data), likely for use in cleansing, validating, or updating address records.


## cleanup_address_entity_0h2

The database table likely manages addresses that have been updated or validated by a third-party service (indicated by 'source_reference', 'paid', and 'source_name') and tracks their validity and updates over time.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| source_reference | VARCHAR(20) | No | Yes |
| entity_identity | VARCHAR(36) | No | Yes |
| paid | VARCHAR(20) | No | Yes |
| source_name | VARCHAR(5) | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| status | VARCHAR(32) | No | Yes |
| full_match_string | VARCHAR(256) | No | Yes |
| version_from_latest | INTEGER | No | Yes |


## cleanup_address_entity_0h2

The database table likely manages addresses that have been updated or validated by a third-party service (indicated by 'source_reference', 'paid', and 'source_name') and tracks their validity and updates over time.


## cleanup_address_entity_0h4

The business purpose of the 'cleanup_address_entity_0h4' table is likely to store and manage data about addresses that need to be removed or updated, based on their matching with other related data sources.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| source_reference | VARCHAR(20) | No | Yes |
| entity_identity | VARCHAR(36) | No | Yes |
| paid | VARCHAR(20) | No | Yes |
| source_name | VARCHAR(5) | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| status | VARCHAR(32) | No | Yes |
| full_match_string | VARCHAR(256) | No | Yes |
| version_from_latest | INTEGER | No | Yes |


## cleanup_address_entity_0h4

The business purpose of the 'cleanup_address_entity_0h4' table is likely to store and manage data about addresses that need to be removed or updated, based on their matching with other related data sources.


## cleanup_address_entity_identity_to_inactive

The business purpose of the 'cleanup_address_entity_identity_to_inactive' database table appears to be mapping and storing inactive entity identities associated with addresses that require cleanup or removal.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | Yes |


## cleanup_address_entity_identity_to_inactive

The business purpose of the 'cleanup_address_entity_identity_to_inactive' database table appears to be mapping and storing inactive entity identities associated with addresses that require cleanup or removal.


## cleanup_address_entity_oa

The business purpose of the 'cleanup_address_entity_oa' database table is to store and manage data related to address entities, specifically tracking their validity, payment status, and history, likely as part of an identity verification or addressing process.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| source_reference | VARCHAR(20) | No | Yes |
| entity_identity | VARCHAR(36) | No | Yes |
| paid | VARCHAR(20) | No | Yes |
| source_name | VARCHAR(5) | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| status | VARCHAR(32) | No | Yes |
| full_match_string | VARCHAR(256) | No | Yes |
| version_from_latest | INTEGER | No | Yes |


## cleanup_address_entity_oa

The business purpose of the 'cleanup_address_entity_oa' database table is to store and manage data related to address entities, specifically tracking their validity, payment status, and history, likely as part of an identity verification or addressing process.


## cleanup_address_entity_republish_update

The business purpose of this database table appears to be tracking and managing updates to addresses that have been previously cleaned or validated across different systems or sources, likely as part of a data quality control process.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| source_reference | VARCHAR(20) | No | Yes |
| entity_identity | VARCHAR(36) | No | Yes |
| paid | VARCHAR(20) | No | Yes |
| source_name | VARCHAR(5) | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| status | VARCHAR(32) | No | Yes |
| full_match_string | VARCHAR(256) | No | Yes |
| version_from_latest | INTEGER | No | Yes |


## cleanup_address_entity_republish_update

The business purpose of this database table appears to be tracking and managing updates to addresses that have been previously cleaned or validated across different systems or sources, likely as part of a data quality control process.


## cleanup_paid_address

The business purpose of a database table named 'cleanup_paid_address' with a column 'paid' likely indicates that it stores information about addresses associated with paid records, where 'paid' might represent whether an address has been assigned to or associated with a specific payment or transaction.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| paid | VARCHAR(20) | No | Yes |


## cleanup_paid_address

The business purpose of a database table named 'cleanup_paid_address' with a column 'paid' likely indicates that it stores information about addresses associated with paid records, where 'paid' might represent whether an address has been assigned to or associated with a specific payment or transaction.


## cleanup_paid_address_entity

The business purpose of a database table named 'cleanup_paid_address_entity' is to store and manage data related to the cleanup of paid addresses, likely in the context of payment processing or invoice management, where each record represents an address associated with a valid payment.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| paid | VARCHAR(20) | No | Yes |
| source_reference | VARCHAR(20) | No | Yes |
| entity_identity | VARCHAR(36) | No | Yes |
| source_name | VARCHAR(5) | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| status | VARCHAR(32) | No | Yes |
| full_match_string | VARCHAR(256) | No | Yes |
| version_from_latest | INTEGER | No | Yes |
| bag_nummeraanduidingidentificatie | VARCHAR(20) | No | Yes |


## cleanup_paid_address_entity

The business purpose of a database table named 'cleanup_paid_address_entity' is to store and manage data related to the cleanup of paid addresses, likely in the context of payment processing or invoice management, where each record represents an address associated with a valid payment.


## cleanup_paid_address_entity_0e2

The database table appears to be tracking payments or subscriptions for individuals (entities) and their corresponding addresses, gathering information on paid transactions, source references, entity identities, and payment statuses with associated verification details.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| paid | VARCHAR(20) | No | Yes |
| source_reference | VARCHAR(20) | No | Yes |
| entity_identity | VARCHAR(36) | No | Yes |
| source_name | VARCHAR(5) | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| status | VARCHAR(32) | No | Yes |
| full_match_string | VARCHAR(256) | No | Yes |
| version_from_latest | INTEGER | No | Yes |
| bag_nummeraanduidingidentificatie | VARCHAR(20) | No | Yes |


## cleanup_paid_address_entity_0e2

The database table appears to be tracking payments or subscriptions for individuals (entities) and their corresponding addresses, gathering information on paid transactions, source references, entity identities, and payment statuses with associated verification details.


## cleanup_paid_address_entity_0e3

The business purpose of the 'cleanup_paid_address_entity_0e3' database table appears to be tracking and managing data related to cleaned-up paid addresses by monitoring their validation status and tracking updates from the latest available source.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| paid | VARCHAR(20) | No | Yes |
| source_reference | VARCHAR(20) | No | Yes |
| entity_identity | VARCHAR(36) | No | Yes |
| source_name | VARCHAR(5) | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| status | VARCHAR(32) | No | Yes |
| full_match_string | VARCHAR(256) | No | Yes |
| version_from_latest | INTEGER | No | Yes |
| bag_nummeraanduidingidentificatie | VARCHAR(20) | No | Yes |


## cleanup_paid_address_entity_0e3

The business purpose of the 'cleanup_paid_address_entity_0e3' database table appears to be tracking and managing data related to cleaned-up paid addresses by monitoring their validation status and tracking updates from the latest available source.


## cleanup_paid_address_entity_republish_update

The business purpose of this database table is to manage the update and re-publishing of cleaned and validated address data records related to paid invoices or transactions, with each record representing a specific payment source and its associated identity.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| paid | VARCHAR(20) | No | Yes |
| source_reference | VARCHAR(20) | No | Yes |
| entity_identity | VARCHAR(36) | No | Yes |
| source_name | VARCHAR(5) | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| status | VARCHAR(32) | No | Yes |
| full_match_string | VARCHAR(256) | No | Yes |
| version_from_latest | INTEGER | No | Yes |
| bag_nummeraanduidingidentificatie | VARCHAR(20) | No | Yes |


## cleanup_paid_address_entity_republish_update

The business purpose of this database table is to manage the update and re-publishing of cleaned and validated address data records related to paid invoices or transactions, with each record representing a specific payment source and its associated identity.


## cleanup_paid_address_entity_withdrawn

The business purpose of this database table appears to be tracking withdrawn payments (identified by the "paid" column) tied to a unique identifier ("entity_identity") and providing detailed information about the withdrawal process.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| paid | VARCHAR(20) | No | Yes |
| source_reference | VARCHAR(20) | No | Yes |
| entity_identity | VARCHAR(36) | No | Yes |
| source_name | VARCHAR(5) | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| status | VARCHAR(32) | No | Yes |
| full_match_string | VARCHAR(256) | No | Yes |
| version_from_latest | INTEGER | No | Yes |
| bag_nummeraanduidingidentificatie | VARCHAR(20) | No | Yes |


## cleanup_paid_address_entity_withdrawn

The business purpose of this database table appears to be tracking withdrawn payments (identified by the "paid" column) tied to a unique identifier ("entity_identity") and providing detailed information about the withdrawal process.


## cleanup_paid_address_with_paid

The primary business purpose of a database table named 'cleanup_paid_address_with_paid' with these columns seems to be cleaning up and standardizing paid addresses from various sources in an organization's customer data.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| paid | VARCHAR(20) | No | Yes |
| source_reference | VARCHAR(20) | No | Yes |
| entity_identity | VARCHAR(36) | No | Yes |
| source_name | VARCHAR(5) | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| status | VARCHAR(32) | No | Yes |


## cleanup_paid_address_with_paid

The primary business purpose of a database table named 'cleanup_paid_address_with_paid' with these columns seems to be cleaning up and standardizing paid addresses from various sources in an organization's customer data.


## del_addresses_sa

The business purpose of a database table named 'del_addresses_sa' appears to be storing and managing address data for specific entities in a jurisdiction (likely South Africa), likely supporting delivery logistics or postal service operations.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | No |
| checksum | VARCHAR(32) | No | Yes |
| status | VARCHAR(32) | No | No |
| source_name | VARCHAR(32) | No | No |
| source_reference | VARCHAR(64) | No | Yes |
| purpose_code | VARCHAR(32) | No | Yes |
| purpose_name | VARCHAR(256) | No | Yes |
| country_code | VARCHAR(32) | No | Yes |
| country_name | VARCHAR(256) | No | Yes |
| state_code | VARCHAR(32) | No | Yes |
| state_name | VARCHAR(256) | No | Yes |
| province_code | VARCHAR(32) | No | Yes |
| province_name | VARCHAR(256) | No | Yes |
| municipality_code | VARCHAR(32) | No | Yes |
| municipality_name | VARCHAR(256) | No | Yes |
| city_code | VARCHAR(32) | No | Yes |
| city_name | VARCHAR(256) | No | Yes |
| district_code | VARCHAR(32) | No | Yes |
| district_name | VARCHAR(256) | No | Yes |
| street_code | VARCHAR(32) | No | Yes |
| street_name | VARCHAR(256) | No | Yes |
| street_number | NUMBER | No | Yes |
| street_type | VARCHAR(256) | No | Yes |
| floor_code | VARCHAR(32) | No | Yes |
| floor_name | VARCHAR(256) | No | Yes |
| floor_number | NUMBER | No | Yes |
| room_code | VARCHAR(32) | No | Yes |
| room_name | VARCHAR(256) | No | Yes |
| room_number | NUMBER | No | Yes |
| door_code | VARCHAR(32) | No | Yes |
| door_name | VARCHAR(256) | No | Yes |
| door_number | NUMBER | No | Yes |
| door_letter | VARCHAR(16) | No | Yes |
| door_prefix | VARCHAR(16) | No | Yes |
| door_suffix | VARCHAR(16) | No | Yes |
| door_type | VARCHAR(256) | No | Yes |
| postal_box | VARCHAR(16) | No | Yes |
| postal_code | VARCHAR(16) | No | Yes |
| boundary | NULL | No | Yes |
| location | NULL | No | Yes |
| valid_from | TIMESTAMP | No | Yes |
| valid_to | TIMESTAMP | No | Yes |
| create_timestamp | TIMESTAMP | No | No |
| update_timestamp | TIMESTAMP | No | Yes |
| fullmatch_key | VARCHAR(512) | No | Yes |
| paid | VARCHAR(24) | No | Yes |
| is_leading | NUMBER | No | Yes |
| validity | VARCHAR(32) | No | Yes |


## del_addresses_sa

The business purpose of a database table named 'del_addresses_sa' appears to be storing and managing address data for specific entities in a jurisdiction (likely South Africa), likely supporting delivery logistics or postal service operations.


## dup_addresses

The business purpose of a database table named 'dup_addresses' with columns 'rn' and 'entity_identity' appears to be storing duplicate addresses associated with entities, where 'rn' likely contains an identifier (e.g. a running number or serial number) and 'entity_identity' represents the entity responsible for the duplicate address.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| rn | NUMBER | No | Yes |
| entity_identity | VARCHAR(36) | No | No |


## dup_addresses

The business purpose of a database table named 'dup_addresses' with columns 'rn' and 'entity_identity' appears to be storing duplicate addresses associated with entities, where 'rn' likely contains an identifier (e.g. a running number or serial number) and 'entity_identity' represents the entity responsible for the duplicate address.


## dups_fullmatch_key_paid

The business purpose of a database table named 'dups_fullmatch_key_paid' with a column named 'fullmatch_key' is likely to store unique identifiers for paid full matches, possibly as part of a ticketing or membership system.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| fullmatch_key | VARCHAR(512) | No | Yes |


## dups_fullmatch_key_paid

The business purpose of a database table named 'dups_fullmatch_key_paid' with a column named 'fullmatch_key' is likely to store unique identifiers for paid full matches, possibly as part of a ticketing or membership system.


## dups_fullmatch_key_paid_orig

The business purpose of a database table named 'dups.fullmatch_key_paid_orig' appears to be identifying and tracking duplicate full-match keys in a payment system, where each row represents a pair of records with the same 'fullmatch_key', differing only by a paid status ('new_paid' vs. 'old_paid') and entity identity.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| fullmatch_key | VARCHAR(512) | No | Yes |
| new_paid | VARCHAR(24) | No | Yes |
| entity_identity | VARCHAR(36) | No | No |
| old_paid | VARCHAR(24) | No | Yes |


## dups_fullmatch_key_paid_orig

The business purpose of a database table named 'dups.fullmatch_key_paid_orig' appears to be identifying and tracking duplicate full-match keys in a payment system, where each row represents a pair of records with the same 'fullmatch_key', differing only by a paid status ('new_paid' vs. 'old_paid') and entity identity.


## dups_paid_fullmatch_key

The business purpose of a database table named 'dups_paid_fullmatch_key' with columns 'paid' likely indicates that it stores a flag to track whether a duplicate payment has been made in full, suggesting an e-commerce or financial application where duplicate payments need to be identified and handled.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| paid | VARCHAR(24) | No | Yes |


## dups_paid_fullmatch_key

The business purpose of a database table named 'dups_paid_fullmatch_key' with columns 'paid' likely indicates that it stores a flag to track whether a duplicate payment has been made in full, suggesting an e-commerce or financial application where duplicate payments need to be identified and handled.


## dups_paid_fullmatch_key_fix

The business purpose of a database table named 'dups_paid_fullmatch_key_fix' appears to be to identify and correct duplicate payments flagged by "fullmatch_key", likely for billing or financial purposes.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| paid | VARCHAR(24) | No | Yes |
| fullmatch_key | VARCHAR(512) | No | Yes |
| new_paid | VARCHAR(4000) | No | Yes |


## dups_paid_fullmatch_key_fix

The business purpose of a database table named 'dups_paid_fullmatch_key_fix' appears to be to identify and correct duplicate payments flagged by "fullmatch_key", likely for billing or financial purposes.


## dups_paid_fullmatch_key_orig

The primary business purpose of a database table named 'dups_paid_fullmatch_key_orig' appears to be identifying duplicate records involving payment status information (paid and newPaid), tracked by entity_identity, possibly for data cleansing or integration purposes.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | No |
| paid | VARCHAR(24) | No | Yes |
| new_paid | VARCHAR(4000) | No | Yes |


## dups_paid_fullmatch_key_orig

The primary business purpose of a database table named 'dups_paid_fullmatch_key_orig' appears to be identifying duplicate records involving payment status information (paid and newPaid), tracked by entity_identity, possibly for data cleansing or integration purposes.


## dups_paid_leading

The database table 'dups_paid_leaking' likely contains data on duplicate payments or entities that have been flagged as paid but should not have been, suggesting an indication of erroneous payment processing.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | No |


## dups_paid_leading

The database table 'dups_paid_leaking' likely contains data on duplicate payments or entities that have been flagged as paid but should not have been, suggesting an indication of erroneous payment processing.


## lavastorm

The business purpose of a database table named 'lavastorm' with the specified columns appears to be storing and managing information related to transactions or events associated with some type of festival (likely a cultural or carnival event), possibly in Canada, as indicated by the country and province codes.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | Yes |
| action | VARCHAR(16) | No | Yes |
| source_name | VARCHAR(16) | No | Yes |
| source_reference | VARCHAR(16) | No | Yes |
| paid | VARCHAR(16) | No | Yes |
| paid_parent | VARCHAR(16) | No | Yes |
| paid_source | VARCHAR(16) | No | Yes |
| country_code | VARCHAR(4) | No | Yes |
| country_name | VARCHAR(32) | No | Yes |
| province_code | VARCHAR(4) | No | Yes |
| province_name | VARCHAR(32) | No | Yes |
| municipality_code | VARCHAR(4) | No | Yes |
| municipality_name | VARCHAR(32) | No | Yes |
| city_code | VARCHAR(4) | No | Yes |
| city_name | VARCHAR(32) | No | Yes |
| street_name | VARCHAR(256) | No | Yes |
| street_name_short | VARCHAR(64) | No | Yes |
| street_type | VARCHAR(32) | No | Yes |
| postal_code | VARCHAR(16) | No | Yes |
| door_number | NUMBER | No | Yes |
| door_letter | VARCHAR(16) | No | Yes |
| door_suffix | VARCHAR(16) | No | Yes |
| room_name | VARCHAR(256) | No | Yes |
| x | NUMBER | No | Yes |
| y | NUMBER | No | Yes |
| note | VARCHAR(4000) | No | Yes |
| line_number | NUMBER | No | Yes |
| group_number | NUMBER | No | Yes |


## lavastorm

The business purpose of a database table named 'lavastorm' with the specified columns appears to be storing and managing information related to transactions or events associated with some type of festival (likely a cultural or carnival event), possibly in Canada, as indicated by the country and province codes.


## lavastorm_location_lookup

The 'lavastorm_location_lookup' database table appears to be a data storage and lookup mechanism for geographically relevant information, such as city locations, streets, postal codes, and coordinates (x, y), likely used in a mapping or logistics-based application, possibly related to the Lavastorm company's business.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| city_code | VARCHAR(128) | No | Yes |
| city_name | VARCHAR(80) | No | Yes |
| street_name | VARCHAR(128) | No | Yes |
| postal_code | VARCHAR(6) | No | Yes |
| door_count | NUMBER | No | Yes |
| x | NUMBER | No | Yes |
| y | NUMBER | No | Yes |
| location | NULL | No | Yes |


## lavastorm_location_lookup

The 'lavastorm_location_lookup' database table appears to be a data storage and lookup mechanism for geographically relevant information, such as city locations, streets, postal codes, and coordinates (x, y), likely used in a mapping or logistics-based application, possibly related to the Lavastorm company's business.


## mdrt_32182$

The business purpose of a database table named 'mdrt_32182$' with columns 'node_id', 'node_level', and 'info' likely lies within network routing configuration management, possibly in an Active Directory or similar system, where this data is used to track and manage device information (node) at specific levels.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| node_id | NUMBER | No | Yes |
| node_level | NUMBER | No | Yes |
| info | BLOB | No | Yes |


## mdrt_32182$

The business purpose of a database table named 'mdrt_32182$' with columns 'node_id', 'node_level', and 'info' likely lies within network routing configuration management, possibly in an Active Directory or similar system, where this data is used to track and manage device information (node) at specific levels.


## mdrt_32183$

The database table `mdrt_32183$` appears to be a temporal or versioning system, likely used for managing and tracking data changes over time, given its timestamp-like nature (`node_id` and `info`) alongside traditional columnar attributes.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| node_id | NUMBER | No | Yes |
| node_level | NUMBER | No | Yes |
| info | BLOB | No | Yes |


## mdrt_32183$

The database table `mdrt_32183$` appears to be a temporal or versioning system, likely used for managing and tracking data changes over time, given its timestamp-like nature (`node_id` and `info`) alongside traditional columnar attributes.


## mdrt_3f006$

The business purpose of a database table named 'mdrt_3f006$' with columns 'node_id', 'node_level', and 'info' likely appears to be a temporary or intermediate storage for metadata related to nodes at various levels in an organizational or hierarchical structure.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| node_id | NUMBER | No | Yes |
| node_level | NUMBER | No | Yes |
| info | BLOB | No | Yes |


## mdrt_3f006$

The business purpose of a database table named 'mdrt_3f006$' with columns 'node_id', 'node_level', and 'info' likely appears to be a temporary or intermediate storage for metadata related to nodes at various levels in an organizational or hierarchical structure.


## mdrt_3f01a$

The database table 'mdrt_3f01a$' likely stores metadata about routing information for Microsoft's Hyper-V platform (MDRT4), with each row corresponding to a network node and containing its ID, level (indicating importance or priority), and associated info.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| node_id | NUMBER | No | Yes |
| node_level | NUMBER | No | Yes |
| info | BLOB | No | Yes |


## mdrt_3f01a$

The database table 'mdrt_3f01a$' likely stores metadata about routing information for Microsoft's Hyper-V platform (MDRT4), with each row corresponding to a network node and containing its ID, level (indicating importance or priority), and associated info.


## metklant

The business purpose of the 'metklant' table with the column 'metklantrow' is likely to store information about customers or clients (metklant), possibly including their contact details or other relevant data that requires row-level access, hinted at by the use of a column named after its row's content.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| metklantrow | VARCHAR(26) | No | Yes |


## metklant

The business purpose of the 'metklant' table with the column 'metklantrow' is likely to store information about customers or clients (metklant), possibly including their contact details or other relevant data that requires row-level access, hinted at by the use of a column named after its row's content.


## mytemppaids

The business purpose of a database table 'mytemppaids' with a column 'mypaids' likely pertains to storage and management of temporary assistance or aid information, such as vouchers or redemption codes, allocated by an organization to its customers or recipients.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| mypaids | VARCHAR(26) | No | Yes |


## mytemppaids

The business purpose of a database table 'mytemppaids' with a column 'mypaids' likely pertains to storage and management of temporary assistance or aid information, such as vouchers or redemption codes, allocated by an organization to its customers or recipients.


## post30_fix_410_delete

The business purpose of a database table named 'post30_fix_410_delete' with columns 'leading_identity', 'previous_identity', and 'type' appears to be tracking and managing the deletion of duplicate or unnecessary posts or documents from a system, possibly as part of an article rewriting or consolidation process.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| leading_identity | VARCHAR(36) | No | No |
| previous_identity | VARCHAR(4000) | No | Yes |
| type | CHAR(20) | No | Yes |


## post30_fix_410_delete

The business purpose of a database table named 'post30_fix_410_delete' with columns 'leading_identity', 'previous_identity', and 'type' appears to be tracking and managing the deletion of duplicate or unnecessary posts or documents from a system, possibly as part of an article rewriting or consolidation process.


## post30_fix_410_delete_sa

The business purpose of this database table appears to be storing fix data related to deleting social accountability (Sa) records at post 30 for a specific legacy application version, presumably as part of an IT migration or archiving process.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| leading_identity | VARCHAR(36) | No | No |
| previous_identity | VARCHAR(4000) | No | Yes |
| type | CHAR(20) | No | Yes |


## post30_fix_410_delete_sa

The business purpose of this database table appears to be storing fix data related to deleting social accountability (Sa) records at post 30 for a specific legacy application version, presumably as part of an IT migration or archiving process.


## post30_fix_data

The primary business purpose of a database table named 'post30_fix_data' with columns 'action', 'entity_identity', 'paid', and 'sources' appears to be data storage and management for post-30 fixes or updates in an online application, likely related to advertising or sponsorship verification.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| action | VARCHAR(128) | No | Yes |
| entity_identity | VARCHAR(128) | No | Yes |
| paid | VARCHAR(26) | No | Yes |
| sources | VARCHAR(26) | No | Yes |


## post30_fix_data

The primary business purpose of a database table named 'post30_fix_data' with columns 'action', 'entity_identity', 'paid', and 'sources' appears to be data storage and management for post-30 fixes or updates in an online application, likely related to advertising or sponsorship verification.


## problematicpaids

The business purpose of a database table named 'problematicpaids' with a single column 'column1' would likely be to track and store problematic payments made by patients, contractors, or other entities, allowing for easy identification and potential rectification of discrepancies.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| column1 | VARCHAR(26) | No | Yes |


## problematicpaids

The business purpose of a database table named 'problematicpaids' with a single column 'column1' would likely be to track and store problematic payments made by patients, contractors, or other entities, allowing for easy identification and potential rectification of discrepancies.


## sa_source_reference

The business purpose of a database table named 'sa_source_reference' with columns: source_reference, new_source_reference appears to be to store and manage references or mappings between an original source information (source_reference) and a modified or equivalent version of that information in the database (new_source_reference), likely for data quality, integration, or transformation purposes.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| source_reference | VARCHAR(64) | No | Yes |
| new_source_reference | VARCHAR(4000) | No | Yes |


## sa_source_reference

The business purpose of a database table named 'sa_source_reference' with columns: source_reference, new_source_reference appears to be to store and manage references or mappings between an original source information (source_reference) and a modified or equivalent version of that information in the database (new_source_reference), likely for data quality, integration, or transformation purposes.


## sa_source_reference_ei

The business purpose of the database table 'sa_source_reference_ei' with columns 'entity_identity', 'old_source_reference', and 'new_source_reference' is to track and store mapping information between a unique external identifier (entity identity) and its corresponding source reference values before and after some change or transformation occurred.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | No |
| old_source_reference | VARCHAR(64) | No | Yes |
| new_source_reference | VARCHAR(4000) | No | Yes |


## sa_source_reference_ei

The business purpose of the database table 'sa_source_reference_ei' with columns 'entity_identity', 'old_source_reference', and 'new_source_reference' is to track and store mapping information between a unique external identifier (entity identity) and its corresponding source reference values before and after some change or transformation occurred.


## saspaids

The business purpose of a database table named 'saspaids' with a single column 'column1' would likely be to store and manage payment information or records related to specific "spa visits" in the SASPA (Spa Payment Assistant) system.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| column1 | VARCHAR(26) | No | Yes |


## saspaids

The business purpose of a database table named 'saspaids' with a single column 'column1' would likely be to store and manage payment information or records related to specific "spa visits" in the SASPA (Spa Payment Assistant) system.


## se_history_audit

The business purpose of a database table named 'se_history_audit' with these columns suggests that it tracks and documents changes (events) to software models (modelid), including audit log activity such as creates, updates, or modifications made by different users or systems (createdby, host), which can be used for auditing, compliance, or troubleshooting purposes.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | No | Yes |
| timestamp | DATE | No | Yes |
| batchid | NUMBER | No | Yes |
| createdby | VARCHAR(64) | No | Yes |
| host | VARCHAR(64) | No | Yes |
| event | VARCHAR(64) | No | Yes |
| description | NCLOB | No | Yes |


## se_history_audit

The business purpose of a database table named 'se_history_audit' with these columns suggests that it tracks and documents changes (events) to software models (modelid), including audit log activity such as creates, updates, or modifications made by different users or systems (createdby, host), which can be used for auditing, compliance, or troubleshooting purposes.


## se_history_batch_info

The business purpose of a database table named 'se_history_batch_info' appears to be to store historical information about batches in a software development lifecycle (Agile and iterative) project management system, where the columns likely track batch-related metadata such as creation, start and end dates, state transitions, and status updates.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | Yes | No |
| batchid | NUMBER | Yes | No |
| creationdate | DATE | No | Yes |
| startdate | DATE | No | Yes |
| enddate | DATE | No | Yes |
| state | VARCHAR(64) | No | Yes |
| statedate | DATE | No | Yes |
| timestamp | DATE | No | Yes |
| lasterror | VARCHAR(256) | No | Yes |


## se_history_batch_info

The business purpose of a database table named 'se_history_batch_info' appears to be to store historical information about batches in a software development lifecycle (Agile and iterative) project management system, where the columns likely track batch-related metadata such as creation, start and end dates, state transitions, and status updates.


## se_history_batch_process

The business purpose of the database table 'se_history_batch_process' appears to be tracking and documenting historical processing batches for some product or service, where each row represents a single batch with associated metadata such as model ID, batch ID, process type, order status, start and end dates, and completion state.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | Yes | No |
| batchid | NUMBER | Yes | No |
| processname | VARCHAR(64) | Yes | No |
| orderid | NUMBER | No | Yes |
| startdate | DATE | No | Yes |
| enddate | DATE | No | Yes |
| state | VARCHAR(64) | No | Yes |
| statedate | DATE | No | Yes |


## se_history_batch_process

The business purpose of the database table 'se_history_batch_process' appears to be tracking and documenting historical processing batches for some product or service, where each row represents a single batch with associated metadata such as model ID, batch ID, process type, order status, start and end dates, and completion state.


## se_history_batch_source

The business purpose of a database table named 'se_history_batch_source' appears to be tracking and storing historical information about various data source batches for model updates or revisions.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | Yes | No |
| batchid | NUMBER | Yes | No |
| name | VARCHAR(256) | Yes | No |
| sourcetype | VARCHAR(64) | No | Yes |
| sourcesubtype | VARCHAR(64) | No | Yes |
| description | VARCHAR(256) | No | Yes |
| xml | VARCHAR(4000) | No | Yes |
| version | VARCHAR(256) | No | Yes |
| versiondate | DATE | No | Yes |


## se_history_batch_source

The business purpose of a database table named 'se_history_batch_source' appears to be tracking and storing historical information about various data source batches for model updates or revisions.


## se_history_model_field

The business purpose of the 'se_history_model_field' database table appears to be tracking changes to model fields over time, storing a audit trail of updates made to schema definitions (models) in a system, likely supporting data model versioning and governance.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | Yes | No |
| tablename | VARCHAR(64) | Yes | No |
| fieldname | VARCHAR(64) | Yes | No |
| tableid | NUMBER | No | Yes |
| externalname | VARCHAR(64) | No | Yes |
| sourcefield | VARCHAR(128) | No | Yes |
| sourcetype | VARCHAR(128) | No | Yes |
| sourcechecksum | VARCHAR(32) | No | Yes |
| validfrom | DATE | No | Yes |
| validto | DATE | No | Yes |
| logicalname | VARCHAR(64) | No | Yes |
| settings | VARCHAR(2000) | No | Yes |
| se_history_ins_batchid | NUMBER | No | Yes |
| se_history_mut_batchid | NUMBER | No | Yes |
| metainfo | NCLOB | No | Yes |


## se_history_model_field

The business purpose of the 'se_history_model_field' database table appears to be tracking changes to model fields over time, storing a audit trail of updates made to schema definitions (models) in a system, likely supporting data model versioning and governance.


## se_history_model_info

The business purpose of a database table named 'se_history_model_info' appears to be tracking changes and metadata for different SQL Server databases (or models), storing information such as model ID, name, SRID settings, and timestamped updates, likely for auditing, versioning, or troubleshooting purposes.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | Yes | No |
| name | VARCHAR(64) | No | Yes |
| srid | NUMBER | No | Yes |
| logicalname | VARCHAR(64) | No | Yes |
| settings | VARCHAR(2000) | No | Yes |
| creationdate | DATE | No | Yes |
| createdby | VARCHAR(64) | No | Yes |
| lastupdate | DATE | No | Yes |
| lastupdatedby | VARCHAR(64) | No | Yes |
| description | VARCHAR(4000) | No | Yes |


## se_history_model_info

The business purpose of a database table named 'se_history_model_info' appears to be tracking changes and metadata for different SQL Server databases (or models), storing information such as model ID, name, SRID settings, and timestamped updates, likely for auditing, versioning, or troubleshooting purposes.


## se_history_model_map

The business purpose of a database table named 'se_history_model_map' with these columns appears to be storing historical mapping data for applications or services that use Geographic Information Systems (GIS) or spatial databases.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | Yes | No |
| maptypeid | NUMBER | Yes | No |
| mapname | VARCHAR(64) | Yes | No |
| mapid | NUMBER | No | Yes |
| bounds | NULL | No | Yes |
| metainfo | NCLOB | No | Yes |


## se_history_model_map

The business purpose of a database table named 'se_history_model_map' with these columns appears to be storing historical mapping data for applications or services that use Geographic Information Systems (GIS) or spatial databases.


## se_history_model_mapfield

The business purpose of the database table 'se_history_model_mapfield' appears to be to store historical mapping records between Salesforce object fields and external data source concepts, likely for data integration or ELT (Extract, Load, Transform) purposes.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | Yes | No |
| maptypeid | NUMBER | Yes | No |
| tablename | VARCHAR(64) | Yes | No |
| fieldname | VARCHAR(64) | Yes | No |
| externalname | VARCHAR(64) | No | Yes |
| fieldid | NUMBER | No | Yes |
| mapfieldname | VARCHAR(64) | No | Yes |
| midfieldname | VARCHAR(64) | No | Yes |


## se_history_model_mapfield

The business purpose of the database table 'se_history_model_mapfield' appears to be to store historical mapping records between Salesforce object fields and external data source concepts, likely for data integration or ELT (Extract, Load, Transform) purposes.


## se_history_model_mapowner

The business purpose of a database table `se_history_model_mapowner` appears to be tracking changes to model owners in a data mapping process across different model types (e.g., tables in an application), storing the historical mapping information for potentially multiple applications or system entities.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | Yes | No |
| maptypeid | NUMBER | Yes | No |
| tablename | VARCHAR(64) | Yes | No |
| fieldname | VARCHAR(64) | Yes | No |


## se_history_model_mapowner

The business purpose of a database table `se_history_model_mapowner` appears to be tracking changes to model owners in a data mapping process across different model types (e.g., tables in an application), storing the historical mapping information for potentially multiple applications or system entities.


## se_history_model_maptype

The business purpose of a database table named 'se_history_model_maptype' appears to be tracking changes or revisions to mapping types (e.g., models associated with specific source data types), likely as part of a larger data management system.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | Yes | No |
| mapsourcename | VARCHAR(64) | Yes | No |
| maptypename | VARCHAR(64) | Yes | No |
| maptypeid | NUMBER | No | Yes |
| externalname | VARCHAR(64) | No | Yes |
| metainfo | NCLOB | No | Yes |


## se_history_model_maptype

The business purpose of a database table named 'se_history_model_maptype' appears to be tracking changes or revisions to mapping types (e.g., models associated with specific source data types), likely as part of a larger data management system.


## se_history_model_table

The business purpose of the 'se_history_model_table' database table appears to be to keep a record of changes made to database models over time, tracking version history and metadata related to each change.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | Yes | No |
| tablename | VARCHAR(64) | Yes | No |
| tableid | NUMBER | No | Yes |
| externalname | VARCHAR(64) | No | Yes |
| sourcetable | VARCHAR(128) | No | Yes |
| sourcechecksum | VARCHAR(32) | No | Yes |
| validfrom | DATE | No | Yes |
| validto | DATE | No | Yes |
| logicalname | VARCHAR(64) | No | Yes |
| settings | VARCHAR(2000) | No | Yes |
| se_history_ins_batchid | NUMBER | No | Yes |
| se_history_mut_batchid | NUMBER | No | Yes |
| metainfo | NCLOB | No | Yes |


## se_history_model_table

The business purpose of the 'se_history_model_table' database table appears to be to keep a record of changes made to database models over time, tracking version history and metadata related to each change.


## se_history_staging_error

The business purpose of a database table named 'se_history_staging_error' is to track and record errors that occurred during ETL (Extract, Transform, Load) process stages, likely in data warehousing or data integration environments.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | Yes | No |
| batchid | NUMBER | Yes | No |
| stagingtablename | VARCHAR(64) | Yes | No |
| sourcekey | VARCHAR(256) | Yes | No |
| stagingtype | VARCHAR(64) | No | Yes |
| errormessage | VARCHAR(4000) | No | Yes |


## se_history_staging_error

The business purpose of a database table named 'se_history_staging_error' is to track and record errors that occurred during ETL (Extract, Transform, Load) process stages, likely in data warehousing or data integration environments.


## se_history_staging_field

The business purpose of a database table named 'se_history_staging_field' is to store versioned records of historical stage field configurations for data modeling and source mapping within the application lifecycle management process.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | Yes | No |
| batchid | NUMBER | Yes | No |
| stagingtablename | VARCHAR(64) | Yes | No |
| stagingfieldname | VARCHAR(64) | Yes | No |
| fieldsourcename | VARCHAR(128) | No | Yes |


## se_history_staging_field

The business purpose of a database table named 'se_history_staging_field' is to store versioned records of historical stage field configurations for data modeling and source mapping within the application lifecycle management process.


## se_history_staging_geom_check

The business purpose of a database table named 'se_history_staging_geom_check' appears to be logging and tracing geometry-related issues or anomalies that occur during the staging process of geospatial (geo) features across different models, tabs, and fields, with the goal of identifying and analyzing potential errors or inconsistencies.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | Yes | No |
| batchid | NUMBER | Yes | No |
| sourcetablename | VARCHAR(128) | Yes | No |
| sourcekey | VARCHAR(256) | Yes | No |
| sourcefieldname | VARCHAR(128) | Yes | No |
| messagetype | VARCHAR(16) | No | Yes |
| message | VARCHAR(4000) | No | Yes |
| data | VARCHAR(4000) | No | Yes |


## se_history_staging_geom_check

The business purpose of a database table named 'se_history_staging_geom_check' appears to be logging and tracing geometry-related issues or anomalies that occur during the staging process of geospatial (geo) features across different models, tabs, and fields, with the goal of identifying and analyzing potential errors or inconsistencies.


## se_history_staging_info

The business purpose of a database table named 'se_history_staging_info' with columns: modelid, batchid, startdate, enddate, state is to store information about the staging process of specific models, including detailed history and status updates such as dates and states.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | Yes | No |
| batchid | NUMBER | Yes | No |
| startdate | DATE | No | Yes |
| enddate | DATE | No | Yes |
| state | VARCHAR(64) | No | Yes |


## se_history_staging_info

The business purpose of a database table named 'se_history_staging_info' with columns: modelid, batchid, startdate, enddate, state is to store information about the staging process of specific models, including detailed history and status updates such as dates and states.


## se_history_staging_mapfield

The business purpose of the 'se_history_staging_mapfield' table appears to be mapping between different data sources and formats, likely used in ETL (Extract, Transform, Load) processes for creating mappings between source data fields and staging tables.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | Yes | No |
| batchid | NUMBER | Yes | No |
| mapsourcename | VARCHAR(64) | Yes | No |
| maptypename | VARCHAR(64) | Yes | No |
| stagingtablename | VARCHAR(64) | Yes | No |
| sourcefieldname | VARCHAR(128) | Yes | No |
| stagingfieldid | NUMBER | No | Yes |
| mapfieldtype | VARCHAR(32) | No | Yes |
| mapfieldname | VARCHAR(64) | No | Yes |
| midfieldname | VARCHAR(64) | No | Yes |
| externalname | VARCHAR(64) | No | Yes |


## se_history_staging_mapfield

The business purpose of the 'se_history_staging_mapfield' table appears to be mapping between different data sources and formats, likely used in ETL (Extract, Transform, Load) processes for creating mappings between source data fields and staging tables.


## se_history_staging_table

The database table 'se_history_staging_table' appears to be used for data warehousing and analytics purposes, storing historical data on the processing, staging, and errors of various data sources and models.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| modelid | NUMBER | Yes | No |
| batchid | NUMBER | Yes | No |
| stagingtablename | VARCHAR(64) | Yes | No |
| tablesourcename | VARCHAR(128) | No | Yes |
| sourcedate | DATE | No | Yes |
| stagingtype | VARCHAR(64) | No | Yes |
| stagingstartdate | DATE | No | Yes |
| stagingenddate | DATE | No | Yes |
| stagingstate | VARCHAR(64) | No | Yes |
| recordcount | NUMBER | No | Yes |
| stagingerrorcount | NUMBER | No | Yes |
| historystartdate | DATE | No | Yes |
| historyenddate | DATE | No | Yes |
| historystate | VARCHAR(64) | No | Yes |
| insertcount | NUMBER | No | Yes |
| updatecount | NUMBER | No | Yes |
| deletecount | NUMBER | No | Yes |
| failurecount | NUMBER | No | Yes |
| errormessage | VARCHAR(3000) | No | Yes |
| staginghistorycommand | NCLOB | No | Yes |


## se_history_staging_table

The database table 'se_history_staging_table' appears to be used for data warehousing and analytics purposes, storing historical data on the processing, staging, and errors of various data sources and models.


## se_history_version_info

The business purpose of a database table named 'se_history_version_info' with columns 'version' and 'description' is likely to store information about different versions of software (e.g. application updates) and the reasons behind each update (e.g. "Fixed Bug", "Added Feature"), providing historical versioning and changelog capabilities.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| version | NUMBER | Yes | No |
| description | VARCHAR(256) | No | Yes |


## se_history_version_info

The business purpose of a database table named 'se_history_version_info' with columns 'version' and 'description' is likely to store information about different versions of software (e.g. application updates) and the reasons behind each update (e.g. "Fixed Bug", "Added Feature"), providing historical versioning and changelog capabilities.


## temptable

The business purpose of a database table named 'temptable' with columns 'paids' likely indicates that payments have been temporarily made or are pending confirmation, suggesting a waiting period before full payment or processing.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| paids | VARCHAR(26) | No | Yes |


## temptable

The business purpose of a database table named 'temptable' with columns 'paids' likely indicates that payments have been temporarily made or are pending confirmation, suggesting a waiting period before full payment or processing.


## vfz_01

The business purpose of a database table named 'vfz_01' appears to be tracking and storing information related to payment processing and customer updates for various entities, such as postal code changes or location overrides.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| entity_identity | VARCHAR(36) | No | Yes |
| entity_identity2 | VARCHAR(36) | No | Yes |
| new_paid | VARCHAR(16) | No | Yes |
| new_postal_code | VARCHAR(6) | No | Yes |
| new_location_override | NULL | No | Yes |
| old_paid | VARCHAR(16) | No | Yes |
| source_reference | VARCHAR(16) | No | Yes |


## vfz_01

The business purpose of a database table named 'vfz_01' appears to be tracking and storing information related to payment processing and customer updates for various entities, such as postal code changes or location overrides.


## zonderklant

I couldn't find any information about the 'zonderklant' database table. However, I can suggest that it might be related to customer data management or handling customer loyalty rewards, where the column 'szonderklantrow' (or without customer row) may store information about customers who don't receive such benefits or rewards, implying that these "without customer" individuals are not necessarily a type of entity in general.

| Column | Type | Primary Key | Nullable |
|--------|------|-------------|----------|
| zonderklantrow | VARCHAR(26) | No | Yes |


## zonderklant

I couldn't find any information about the 'zonderklant' database table. However, I can suggest that it might be related to customer data management or handling customer loyalty rewards, where the column 'szonderklantrow' (or without customer row) may store information about customers who don't receive such benefits or rewards, implying that these "without customer" individuals are not necessarily a type of entity in general.



# Relationships


### address_attribute.parent_identity → address.entity_identity

The relationship between the database tables 'address_attribute' and 'address' is a one-to-one reference, as addressed_attribute.["parent_identity"] uniquely corresponds to the entity identified by address["entity_identity"], indicating that each address has a corresponding attribute set while each attribute set belongs to exactly one address domain data type.

It would be beneficial for clarity for some examples or instances of how this actually works with real examples as well


### address_diagnostic.parent_identity → address.entity_identity

The relationship between 'address_diagnostic' and 'address' is a one-to-many relationship, where each address can have multiple diagnostic records (i.e., an address may appear in the 'parent_identity' column of many 'address_diagnostic' rows), but not necessarily vice versa.


### address_event.user_identity → USER.entity_identity

The relationship between database tables 'address_event' and 'USER' is a many-to-many relationship, as the foreign key 'user_identity' in 'address_event' references the primary key 'entity_identity' in 'USER', indicating that multiple users can be associated with multiple events and vice versa.


### address_event.parent_identity → address.entity_identity

The relationship between `address_event` and `address` is a one-to-many relationship, as the same `entity_identity` (i.e., an address) can have multiple corresponding records in `address_event`.


### address_relation.source_identity → address.entity_identity

The relationship between 'address Relation' and 'address' in this scenario is a one-to-many, as the 'source_identity' within 'address_relation' can reference multiple addresses (one address per record in 'address_relation'), making 'address_relation' dependent on but not exclusively linked to 'address'.


### address_relation.target_identity → address.entity_identity

The relationship between 'address Relation' and 'address' in this scenario is a one-to-many, as the 'source_identity' within 'address_relation' can reference multiple addresses (one address per record in 'address_relation'), making 'address_relation' dependent on but not exclusively linked to 'address'.

