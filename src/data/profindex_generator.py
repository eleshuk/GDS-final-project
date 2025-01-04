import pandas as pd
import numpy as np

# Caminhos dos ficheiros
marketdata_file = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\StockMarket\MarketData.xlsx"
crop_file = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\StockMarket\crops_table.csv"
output_file = r"C:\Users\Luís Pinto Coelho\Documents\MGDS\DMS\StockMarket\Crop_with_ProfitabilityIndex.csv"

# Dicionário com fatores de impacto econômico para todas as 94 culturas
economic_impact = {
    "almond": 0.15, "apples": 0.1, "apricots": 0.05, "asparagus": 0.05, "avocados": 0.1,
    "banana": 0.1, "barley": 0.05, "bean": 0.05, "beans__green": 0.05, "blueberries": 0.15,
    "broad_beans": 0.05, "broad_beans_and_horse_beans__green": 0.05, "cabbages": 0.1,
    "carrots_and_turnips": 0.1, "cauliflowers_and_broccoli": 0.05, "cereal": 0.1,
    "cereals_n_e_c_": 0.05, "cherries": 0.15, "chestnut": 0.1, "chickpeas": 0.05,
    "chillies_and_peppers__green__capsicum_spp__and_pimenta_spp_": 0.1, "citrus_fruit": 0.15,
    "cucumbers_and_gherkins": 0.1, "currants": 0.05, "eggplants": 0.05, "fibre_crops__fibre_equivalent": 0.05,
    "figs": 0.1, "flax__raw_or_retted": 0.05, "fruit": 0.1, "garlic": 0.1, "grapefruit": 0.1,
    "grapes": 0.2, "groundnut": 0.05, "hazelnuts": 0.1, "hempseed": 0.05, "hop_cones": 0.0,
    "kiwi": 0.15, "leeks": 0.05, "lemons_and_limes": 0.1, "lettuce": 0.05, "linseed": 0.05,
    "locust_beans__carobs_": 0.05, "lupins": 0.05, "maize": 0.1, "melon": 0.1, "millet": 0.05,
    "oats": 0.05, "oilcrops__cake_equivalent": 0.05, "oilcrops__oil_equivalent": 0.05,
    "olives": 0.2, "onions": 0.1, "onions_and_shallots__green": 0.05, "orange": 0.15,
    "other_berries_and_fruits_of_the_genus_vaccinium_n_e_c_": 0.05, "other_fruits__n_e_c_": 0.05,
    "other_nuts__excluding_wild_edible_nuts_and_groundnuts__in_shell__n_e_c_": 0.05,
    "other_pome_fruits": 0.05, "other_pulses_n_e_c_": 0.05, "other_stone_fruits": 0.05,
    "other_vegetables__fresh_n_e_c_": 0.05, "peaches_and_nectarines": 0.1, "pears": 0.1,
    "peas__green": 0.05, "pineapples": 0.1, "plums": 0.1, "potato": 0.1, "pulses": 0.05,
    "pumpkins__squash_and_gourds": 0.05, "quinces": 0.0, "raspberries": 0.1, "rice": 0.1,
    "roots_and_tubers": 0.05, "rye": 0.05, "safflower_seed": 0.05, "sour_cherries": 0.05,
    "spinach": 0.05, "strawberries": 0.15, "sugar_crops": 0.1, "sugarbeet": 0.1, "sugarcane": 0.1,
    "sunflower": 0.1, "sweet_potatoes": 0.05, "tangerines": 0.15, "tea": 0.05, "tobacco": 0.05,
    "tomato": 0.1, "treenuts": 0.05, "triticale": 0.05, "true_hemp__raw_or_retted": 0.05,
    "vegetables": 0.1, "walnuts": 0.1, "watermelons": 0.1, "wheat": 0.15, "yams": 0.05
}

# Função para calcular o Profitability Index
def calculate_profitability(crop_name, marketdata):
    # Filtrar os dados do MarketData para o CropName específico
    crop_data = marketdata[marketdata["CropName"] == crop_name]
    if crop_data.empty:
        return 0.5  # Valor padrão para culturas sem dados
    
    # Remover outliers (percentil 5% a 95%)
    price_filtered = crop_data["PricePerTon"].clip(
        lower=crop_data["PricePerTon"].quantile(0.05),
        upper=crop_data["PricePerTon"].quantile(0.95)
    )
    demand_filtered = crop_data["DemandIndex"].clip(
        lower=crop_data["DemandIndex"].quantile(0.05),
        upper=crop_data["DemandIndex"].quantile(0.95)
    )
    
    # Cálculo da média dos dados filtrados
    avg_price = price_filtered.mean()
    avg_demand = demand_filtered.mean()
    
    # Máximos para normalizar
    max_price = marketdata["PricePerTon"].max()
    
    # Pesos para PricePerTon e DemandIndex
    price_weight = 0.3
    demand_weight = 0.5

    # Fator de impacto econômico com ampliação de peso
    impact_factor = economic_impact.get(crop_name, 0.0) * 1.5

    # Introduzir flutuação aleatória controlada
    random_fluctuation = np.random.uniform(-0.05, 0.05)
    
    # Calcular o Profitability Index
    profitability_index = (
        (avg_price / max_price) * price_weight +
        avg_demand * demand_weight +
        impact_factor +
        random_fluctuation
    )
    return round(min(max(profitability_index, 0.0), 1.0), 2)  # Garante que o índice está entre 0 e 1

# Carregar os dados
marketdata_df = pd.read_excel(marketdata_file)
crop_df = pd.read_csv(crop_file, sep=";")

# Normalizar os nomes das culturas para evitar problemas de correspondência
marketdata_df["CropName"] = marketdata_df["CropName"].str.strip().str.lower()
crop_df["Name"] = crop_df["Name"].str.strip().str.lower()

# Aplicar o cálculo para cada cultura no Crop usando o Name (relacionado ao CropName)
crop_df["ProfitabilityIndex"] = crop_df["Name"].apply(
    lambda crop_name: calculate_profitability(crop_name, marketdata_df)
)

# Salvar o ficheiro atualizado
crop_df.to_csv(output_file, sep=";", index=False)

print(f"Dados atualizados e salvos em: {output_file}")
