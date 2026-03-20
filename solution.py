import pandas as pd


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str ) -> pd.DataFrame:
    #validation of new column name
    if not all(c.isalpha() or c == "_" for c in new_column):
        return pd.DataFrame([])

    #validation of role
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_ +-*")
    if not all(c in allowed_chars for c in role):
        return pd.DataFrame([])

    #check if every column in role exists in dataframe and is correct
    tokens = role.replace("+"," ").replace("-"," ").replace("*"," ").split()
    for token in tokens:
        if not token.replace("_","").isdigit():
            if not all(c.isalpha() or c == "_" for c in token):
                return pd.DataFrame([])
            if token not in df.columns:
                return pd.DataFrame([])

    #new column
    try:
        df = df.copy()
        df[new_column] = df.eval(role)
    except Exception:
        return pd.DataFrame([])

    return df