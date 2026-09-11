import marimo

__generated_with = "0.24.0"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Data loading and first look

    **Dataset:** Diabetes 130-US Hospitals for Years 1999-2008 Dataset (https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008) (100766 patients, 47 features)

    **Goal:** Identify clinical patterns that distinguish readmitted patients

    **Author:** Nasir Nesirli

    **Tools:** Python, Pandas, Matplotlib, Seaborn
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Data Dictionary

    | Variable Name | Description |
    | :--- | :--- |
    | **encounter_id** | Unique identifier of an encounter |
    | **patient_nbr** | Unique identifier of a patient |
    | **race** | Values: Caucasian, Asian, African American, Hispanic, and other |
    | **gender** | Values: male, female, and unknown/invalid |
    | **age** | Grouped in 10-year intervals: [0, 10), [10, 20),..., [90, 100) |
    | **weight** | Weight in pounds. |
    | **admission_type_id** | Integer identifier corresponding to 9 distinct values, for example, emergency, urgent, elective, newborn, and not available |
    | **discharge_disposition_id** | Integer identifier corresponding to 29 distinct values, for example, discharged to home, expired, and not available |
    | **admission_source_id** | Integer identifier corresponding to 21 distinct values, for example, physician referral, emergency room, and transfer from a hospital |
    | **time_in_hospital** | Integer number of days between admission and discharge |
    | **payer_code** | Integer identifier corresponding to 23 distinct values, for example, Blue Cross/Blue Shield, Medicare, and self-pay |
    | **medical_specialty** | Integer identifier of a specialty of the admitting physician, corresponding to 84 distinct values, for example, cardiology, internal medicine, family/general practice, and surgeon |
    | **num_lab_procedures** | Number of lab tests performed during the encounter |
    | **num_procedures** | Number of procedures (other than lab tests) performed during the encounter |
    | **num_medications** | Number of distinct generic names administered during the encounter |
    | **number_outpatient** | Number of outpatient visits of the patient in the year preceding the encounter |
    | **number_emergency** | Number of emergency visits of the patient in the year preceding the encounter |
    | **number_inpatient** | Number of inpatient visits of the patient in the year preceding the encounter |
    | **diag_1** | The primary diagnosis (coded as first three digits of ICD9); 848 distinct values |
    | **diag_2** | Secondary diagnosis (coded as first three digits of ICD9); 923 distinct values |
    | **diag_3** | Additional secondary diagnosis (coded as first three digits of ICD9); 954 distinct values |
    | **number_diagnoses** | Number of diagnoses entered to the system |
    | **max_glu_serum** | Indicates the range of the result or if the test was not taken. Values: >200, >300, normal, and none if not measured |
    | **A1Cresult** | Indicates the range of the result or if the test was not taken. Values: >8 if the result was greater than 8%, >7 if the result was greater than 7% but less than 8%, normal if the result was less than 7%, and none if not measured. |
    | **metformin** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **repaglinide** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **nateglinide** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **chlorpropamide** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **glimepiride** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **acetohexamide** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **glipizide** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **glyburide** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **tolbutamide** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **pioglitazone** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **rosiglitazone** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **acarbose** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **miglitol** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **troglitazone** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **tolazamide** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **examide** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **citoglipton** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **insulin** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **glyburide-metformin** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **glipizide-metformin** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **glimepiride-pioglitazone** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **metformin-rosiglitazone** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **metformin-pioglitazone** | The feature indicates whether the drug was prescribed or there was a change in the dosage. Values: up if the dosage was increased during the encounter, down if the dosage was decreased, steady if the dosage did not change, and no if the drug was not prescribed |
    | **change** | Indicates if there was a change in diabetic medications (either dosage or generic name). Values: change and no change |
    | **diabetesMed** | Indicates if there was any diabetic medication prescribed. Values: yes and no |
    | **readmitted** | Days to inpatient readmission. Values: <30 if the patient was readmitted in less than 30 days, >30 if the patient was readmitted in more than 30 days, and No for no record of readmission. |
    """)
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import missingno as msno

    from diabetes_readmission.ingest.get_data import load_data

    sns.set_theme(style="whitegrid", palette="muted")
    plt.rcParams["figure.figsize"] = (10, 5)
    plt.rcParams["axes.spines.top"] = False
    plt.rcParams["axes.spines.right"] = False
    return load_data, msno, np, pd, plt, sns


@app.cell
def _(load_data):
    df = load_data()

    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    return (df,)


@app.cell
def _(df):
    df.head().T
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Data quality assessment
    """)
    return


@app.cell
def _(df):
    # Dtypes
    print("Dtypes: ")
    print(df.dtypes)

    print("====================================")

    # Missing values
    print("Missing values: ")
    print(df.isnull().sum())

    print("====================================")

    # Duplicate rows
    print("Duplicate rows: ")
    print(df.duplicated().sum())
    return


@app.cell
def _(df, pd):
    # Where exactly are the missing values?
    missing = df.isnull().sum()
    missing_pct = missing / len(df) * 100
    _missing_df = pd.DataFrame({'count': missing, 'pct': missing_pct}).query('count > 0')
    print(_missing_df)
    return


@app.cell
def _(df, msno):
    msno.matrix(df)
    return


@app.cell
def _(df, msno):
    msno.heatmap(df)
    return


@app.cell
def _(df):
    # Check correlation of missing values
    _missing_df = df.isnull()
    missing_corr = _missing_df.corr()
    print(missing_corr)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - All of the correlation numbers are very close to zero, there are no strong structural patterns of missingness between the columns themselves.

    - The missingness across features is happening independently.
    """)
    return


@app.cell
def _(df):
    # Renaming columns for better readability
    df.columns = df.columns.str.replace("-", "_").str.lower()
    return


@app.cell
def _(df):
    # Select categorical columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    for _col in categorical_cols:
    # Convert categorical columns to lowercase
        df[_col] = df[_col].str.lower()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Handling missing values
    """)
    return


@app.cell
def _(df):
    for _col in df.columns:
        print(df[_col].value_counts())
        print('====================================')
    return


@app.cell
def _(df):
    # Filling missing values in race column with "unknown"
    df['race'].fillna(value="unknown", inplace=True)

    # Dropping weight column as it has 97% missing values
    df.drop(columns=["weight"], inplace=True)

    # Filling missing values in payer_code, medical_specialty, diag_1, diag_2, and diag_3 columns with "unknown"
    df[["payer_code", "medical_specialty", "diag_1", "diag_2", "diag_3"]] = df[["payer_code", "medical_specialty", "diag_1", "diag_2", "diag_3"]].fillna("unknown")

    # Filling missing values in a1cresult column with "not_measured" (stated in the data dictionary)
    df['a1cresult'].fillna(value="not_measured", inplace=True)

    # Filling missing values in max_glu_serum column with "not_measured" (stated in the data dictionary)
    df['max_glu_serum'].fillna(value="not_measured", inplace=True)
    return


@app.cell
def _(df):
    df.isnull().sum().sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Univariate analysis
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Target Variable
    """)
    return


@app.cell
def _(df):
    target_counts = df['readmitted'].value_counts()
    target_pct = (target_counts / len(df)) * 100

    print(f"Target value distribution:\n{target_counts}\n{target_pct}")
    return (target_counts,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Targets are imbalanced. Should be considered during modelling.
    """)
    return


@app.cell
def _(plt, target_counts):
    _fig, _ax = plt.subplots()
    _ax.bar(target_counts.index, target_counts.values)
    _ax.set_title('Target Value Distribution')
    _ax.set_xlabel('Readmitted')
    _ax.set_ylabel('Count')
    for _i, v in enumerate(target_counts.values):
        _ax.text(_i, v + 2, str(v), ha='center', fontsize=11)
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Numeric feature distributions
    """)
    return


@app.cell
def _(df, plt):
    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    _fig, _axes = plt.subplots(4, 3, figsize=(15, 12))
    _axes = _axes.flatten()
    for _i, _col in enumerate(num_cols):
        _axes[_i].hist(df[_col], bins=10, color='steelblue', edgecolor='white')
        _axes[_i].set_title(_col)
        _axes[_i].set_ylabel('Count')
        mean_value = df[_col].mean()
        _axes[_i].axvline(mean_value, color='coral', linestyle='--', linewidth=1.5)
        _axes[_i].text(mean_value, _axes[_i].get_ylim()[1] * 0.9, f'mean={mean_value:.0f}')
    _axes[11].set_visible = False
    plt.suptitle('Numeric feature distributions', y=1.02)
    plt.tight_layout()
    plt.show()
    return (num_cols,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Categorical feature distributions
    """)
    return


@app.cell
def _(df):
    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    len(cat_cols)
    return (cat_cols,)


@app.cell
def _(cat_cols, df, plt, sns):
    # Isolate and remove high-cardinality columns so they don't break the grid
    high_cardinality_cols = ['diag_1', 'diag_2', 'diag_3', 'medical_specialty', 'encounter_id', 'patient_nbr']
    med_cols = ['metformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 'acetohexamide', 'glipizide', 'glyburide', 'tolbutamide', 'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol', 'troglitazone', 'tolazamide', 'examide', 'citoglipton', 'insulin', 'glyburide_metformin', 'glipizide_metformin', 'glimepiride_pioglitazone', 'metformin_rosiglitazone', 'metformin_pioglitazone']
    # Medication columns
    plot_cols = [_col for _col in cat_cols if _col not in high_cardinality_cols and _col not in med_cols]
    num_plots = len(plot_cols)
    num_rows = (num_plots + 2) // 3
    _fig, _axes = plt.subplots(num_rows, 3, figsize=(18, num_rows * 3.5))
    _axes = _axes.flatten()
    for _i, _col in enumerate(plot_cols):
        sns.countplot(data=df, y=_col, ax=_axes[_i], color='steelblue')
        _axes[_i].set_title(_col, fontsize=12, fontweight='bold')
        _axes[_i].set_xlabel('Count')
        _axes[_i].set_ylabel('')
    for _j in range(_i + 1, len(_axes)):
        _fig.delaxes(_axes[_j])
    plt.tight_layout()
    plt.show()
    return med_cols, num_rows, plot_cols


@app.cell
def _(df, med_cols, pd, plt):
    med_counts = df[med_cols].apply(pd.Series.value_counts).fillna(0).T
    ordered_categories = ['no', 'steady', 'up', 'down']
    existing_cats = [cat for cat in ordered_categories if cat in med_counts.columns]
    med_counts = med_counts[existing_cats]
    colors = ['#e0e0e0', '#2ca02c', '#ff7f0e', '#d62728']
    _ax = med_counts.plot(kind='barh', stacked=True, figsize=(12, 10), color=colors[:len(existing_cats)], edgecolor='white')
    plt.title('Diabetic Medication Prescriptions and Dosage Changes', fontsize=14, fontweight='bold')
    plt.xlabel('Number of Patients', fontsize=12)
    plt.ylabel('Medication', fontsize=12)
    plt.legend(title='Dosage Status', bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Descriptive statistics
    """)
    return


@app.cell
def _(df):
    summary = df.describe().round(1)
    summary.T
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Bivariate analysis
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Numeric features vs readmission
    """)
    return


@app.cell
def _(df, num_cols, plt, sns):
    _fig, _axes = plt.subplots(4, 3, figsize=(15, 12))
    _axes = _axes.flatten()
    for _i, _col in enumerate(num_cols):
        sns.boxplot(data=df, x='readmitted', y=_col, ax=_axes[_i], palette={'no': 'steelblue', '<30': 'red', '>30': 'orange'}, hue='readmitted')
        _axes[_i].set_title(f'{_col} by readmission status', fontsize=12, fontweight='bold')
        _axes[_i].set_xlabel('Readmission Status')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(df, num_rows, pd, plot_cols, plt):
    _fig, _axes = plt.subplots(num_rows, 3, figsize=(18, num_rows * 3.5))
    _axes = _axes.flatten()
    color_map = {'no': 'steelblue', '<30': 'red', '>30': 'coral'}
    for _i, _col in enumerate(plot_cols):
        ct = pd.crosstab(df[_col], df['readmitted'], normalize='index') * 100
        ct.plot(kind='bar', ax=_axes[_i], color=color_map, edgecolor='white')
        _axes[_i].set_title(f'{_col} vs readmission')
        _axes[_i].set_xlabel('')
        _axes[_i].set_ylabel('Percentage %')
        _axes[_i].tick_params(axis='x', rotation=0)
        _axes[_i].legend(title='readmitted', fontsize=8)
    for _j in range(len(plot_cols), len(_axes)):
        _fig.delaxes(_axes[_j])
    plt.suptitle('Categorical features vs readmission status', y=1.02)
    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. Multivariate analysis
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Correlation matrix
    """)
    return


@app.cell
def _(df, np, plt, sns):
    # Encode target for correlation
    df_corr = df.copy()
    _numeric_df = df_corr.select_dtypes(include=np.number)
    # Numeric columns only
    _corr_matrix = _numeric_df.corr()
    _fig, _ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(_corr_matrix, annot=True, cmap='coolwarm', center=0, ax=_ax)
    plt.title('Correlation matrix of numeric features')
    plt.tight_layout()
    plt.show()
    return (df_corr,)


@app.cell
def _(df_corr, np):
    df_corr['readmitted'] = df_corr['readmitted'].map({'no': 0, '<30': 1, '>30': 2})
    _numeric_df = df_corr.select_dtypes(include=np.number)
    _corr_matrix = _numeric_df.corr()
    target_corr = _corr_matrix['readmitted'].drop('readmitted').sort_values(ascending=False)
    # Correlation of every numeric feature WITH the target, sorted
    print(target_corr)
    return


@app.cell
def _(df, pd):
    from sklearn.feature_selection import mutual_info_classif
    from sklearn.preprocessing import LabelEncoder
    X = df.drop(columns='readmitted').copy()
    y = LabelEncoder().fit_transform(df['readmitted'])
    cat_idx = []
    for _i, _col in enumerate(X.columns):
    # Label-encode categoricals and flag them as discrete
        if X[_col].dtype == 'object':
            X[_col] = LabelEncoder().fit_transform(X[_col].astype(str))
            cat_idx.append(True)
        else:
            cat_idx.append(False)
    mi = mutual_info_classif(X, y, discrete_features=cat_idx, random_state=0)
    mi_scores = pd.Series(mi, index=X.columns).sort_values(ascending=False)
    print(mi_scores)
    return X, y


@app.cell
def _(X, pd, y):
    from sklearn.ensemble import RandomForestClassifier

    rf = RandomForestClassifier(n_estimators=200, max_depth=12,
                                class_weight='balanced', n_jobs=-1, random_state=0)
    rf.fit(X, y)

    importances = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)
    print(importances.head(15))
    return (rf,)


@app.cell
def _(X, pd, rf, y):
    from sklearn.inspection import permutation_importance
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import make_scorer, roc_auc_score

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, stratify=y, random_state=0)

    auc_ovr = make_scorer(
        roc_auc_score,
        multi_class='ovr',
        average='macro',
        response_method='predict_proba'
    )

    perm = permutation_importance(
        rf, X_test, y_test,
        n_repeats=10, random_state=0, n_jobs=-1,
        scoring=auc_ovr
    )

    perm_imp = pd.Series(perm.importances_mean, index=X.columns).sort_values(ascending=False)
    print(perm_imp.head(15))
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(df):
    df.race.value_counts()
    return


@app.cell
def _(df):
    f1 = df.race
    f1 = f1.map({'caucasian': 1, 'africanamerican': 2, 'unknown':3, 'hispanic':4, 'other':5, 'asian':6})
    return (f1,)


@app.cell
def _(f1):
    f1.var()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. Clinical insights summary
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 7. Next steps
    """)
    return


if __name__ == "__main__":
    app.run()
