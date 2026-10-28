def convert_date_format(date_str, input_format, output_format):
    """
    Convert a date string from one format to another.

    :param date_str: The date string to convert.
    :param input_format: The format of the input date string.
    :param output_format: The desired format for the output date string.
    :return: The converted date string in the desired format.
    """
    from datetime import datetime

    # Parse the input date string into a datetime object
    date_obj = datetime.strptime(date_str, input_format)

    # Format the datetime object into the desired output format
    return date_obj.strftime(output_format)