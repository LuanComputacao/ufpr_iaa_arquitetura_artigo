from kdd import df_body_fat, heat_map_analysis, show_attibute_relations


def main():
    show_attibute_relations(df_body_fat, 'BodyFat')
    heat_map_analysis(df_body_fat)


if __name__ == '__main__':
    main()
