library(dplyr)

# Definition groupement segment
vip <- c("V")
group_1 <- c("A", "B")
group_2 <- c("C", "D")

# Create dummy dataframe
# avec annee
tbl <- tibble(
  year = rep(c(2019, 2020), 5),
  segment  = factor(
    rep(c("V", "A", "B", "C", "D"), each  = 2),
    levels = c("V", "A", "B", "C", "D")
    ),
  nbr = 1:10
)

# Groupement par segment (sans annee)
tbl %>%
  group_by(segment) %>%
  summarise(total_segment = sum(nbr))

# Groupement par segment (sans annee)
tbl %>%
  # Creation d'une nouvelle variable
  # pour definir les groupements de segments
  mutate(groupement_segment = case_when(
    segment %in% vip ~ "VIP",
    segment %in% group_1 ~ "actif",
    segment %in% group_2 ~ "inactif",
    # "else" si un segment n'est pas reference dans l'init
    TRUE ~ "not assigned"
  )) %>%
  # Aggregat par groupement de segment
  group_by(groupement_segment) %>%
  summarise(total_group = sum(nbr))

# Groupement par segment (avec annee)
tbl %>%
  # Creation d'une nouvelle variable
  # pour definir les groupements de segments
  mutate(groupement_segment = case_when(
    segment %in% vip ~ "VIP",
    segment %in% group_1 ~ "actif",
    segment %in% group_2 ~ "inactif",
    # "else" si un segment n'est pas reference dans l'init
    TRUE ~ "not assigned"
  )) %>%
  # Aggregat par groupement de segment et par annee
  group_by(year, groupement_segment) %>%
  summarise(total_group = sum(nbr))
