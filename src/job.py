def transform(df):
    # Intentional bad practice for AI review
    data = df.collect()
    return data
