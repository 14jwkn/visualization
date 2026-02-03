library(tidyverse)
library(ggplot2)

# Load dataset.
df <- read_csv('toronto-shelter-system-flow.csv')

# Change date name for ease.
colnames(df)[colnames(df)=='date(mmm-yy)'] <- 'date'

# Extract only all population to avoid duplication.
df = df[df[,'population_group']=='All Population',]

# Extract the year only and group by it, then calculate mean and standard error
# across months for that year.
df_stats <- df %>%
  mutate(year=str_sub(date,-2)) %>%
  group_by(year) %>%
  summarize(
    avg_identified=mean(newly_identified),
    sd_identified=sd(newly_identified),
    n = n()
  ) %>%
  mutate(se_identified=sd_identified/sqrt(n))

# Plot newly identified homeless over time.
p <- ggplot(df,aes(x=year,y=avg_identified)) +
  geom_col(fill='steelblue') +
  geom_errorbar(aes(ymin=avg_identified-se_identified, 
                    ymax=avg_identified+se_identified), 
                width=0.2,color='red') +
  labs(title='Newly Identified Individuals Experiencing Homelessness in Toronto Over Time',
       x='Year',
       y='Number of Individuals') +
  theme_minimal() +
  theme(axis.text.x = element_text(angle=90,hjust = 1))

