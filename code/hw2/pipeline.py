def fetch_gdif_data(species_list, year):
    """
    retrieves observations from GBIF API
    returns DataFrame with at min species name, coordinates, date, state,
    and coordinate uncertainty
    """
    pass

def clean_biodiversity_data(raw_df):
    """
    removes invalid/missing data
    removes duplicates and invalid data
    extracts month from dates
    returns cleaned DataFrame and
    a metrics dictionary quantifying what was removed
    :param raw_df:
    :return:
    """
    pass

def enrich_with_state_data(cleaned_df, state_ref_df):
    """
    joins observations with state reference data
    """
    pass

def calculate_analysis(enriched_df):
    """
    performs analysis
    obervations per state with density
    species distribution across months as a plot 
    :param enriched_df:
    :return:
    """

def main():
    """
    Main function to run all demonstrations
    """

if __name__ == "__main__":
    main()
